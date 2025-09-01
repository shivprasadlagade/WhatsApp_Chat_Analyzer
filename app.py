import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns


st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt", "csv"])
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocessor(data)

    # Data Info
    st.write("Columns detected:")
    st.write(df.head(6))
    user_col = 'sender'
    # For example, if 'sender' is the actual column:
    user_list = df[user_col].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)
    if st.sidebar.button("Show Analysis"):

        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        #This stats for the all conversation between participants::

        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)

            with col2:
                st.header("Total Words")
                st.title(words)

            with col3:
                st.header("Total Media Messages")
                st.title(num_media_messages)

            with col4:
                st.header("Total Links")
                st.title(num_links)

            # Finding busy person
            if selected_user == "Overall":
                st.title('Most Busy Guy!')
                x , new_df= helper.most_busy_user(df)
                fig, ax = plt.subplots()
                col1, col2=st.columns(2)

                with col1:
                    ax.bar(x.index, x.values, color='red')
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)
                with col2:
                    st.dataframe(new_df)
        #----------------------------Wordcloud---------------------------------------------------
        st.title("Word cloud")
        df_wc= helper.create_wordcloud(selected_user,df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

      #--------------------------Emoji Analysis--------------------------------------------------

    st.title("Emoji Analysis")
    emoji_df = helper.emoji_helper(selected_user, df)
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(emoji_df)
    with col2:
        import matplotlib
        matplotlib.rcParams['font.family'] = 'Segoe UI Emoji'
        top_emoji_df = emoji_df.head(6)
        fig, ax = plt.subplots()
        ax.pie(top_emoji_df['count'], labels=top_emoji_df['emoji'], autopct='%0.2f%%')
        st.pyplot(fig)
