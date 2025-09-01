import re
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
import emoji
from urlextract import URLExtract
from emoji import EMOJI_DATA
extractor = URLExtract()

def fetch_stats(selected_user, df):
    # Pick correct user column name
    user_col = 'user'  # default

    if 'user' not in df.columns:
        if 'sender' in df.columns:
            user_col = 'sender'
        else:
            # Column missing - cannot proceed
            return 0, 0, 0, 0

    if selected_user == "Overall":
        df_user = df
    else:
        df_user = df[df[user_col] == selected_user]

    num_messages = df_user.shape[0]
    words = sum(len(str(message).split()) for message in df_user['message'])
    num_media_messages = df_user[df_user['message'].str.contains('<Media omitted>', na=False)].shape[0]
    url_pattern = r'(https?://\S+)'
    num_links = df_user['message'].str.contains(url_pattern, regex=True, na=False).sum()

    return num_messages, words, num_media_messages, num_links

def most_busy_user(df):
    x = df['sender'].value_counts().head()
    df=round((df['sender'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'sender': 'name'})
    return x,df

def create_wordcloud(selected_user, df):
    if  selected_user != 'Overall':
        df=df[df['sender'] == selected_user]

    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc=wc.generate(df['message'].str.cat(sep=''))
    return df_wc

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['sender'] == selected_user]

    emojis = []
    for message in df['message']:
        if isinstance(message, str):
            emojis.extend([c for c in message if c in EMOJI_DATA])

    emoji_counts = Counter(emojis)
    emoji_df = pd.DataFrame(emoji_counts.most_common(), columns=['emoji', 'count'])
    return emoji_df
