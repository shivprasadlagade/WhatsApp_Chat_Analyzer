------------------------WhatsApp Chat Analyzer (Streamlit)====================================================
A Streamlit-based WhatsApp Chat Analyzer that lets users upload exported chats to view chat statistics, wordclouds, busiest participant charts, and emoji usage with interactive visuals.
Includes overall and per-user insights: totals (messages, words, media, links), “Most Busy” bar chart with a detailed table, word frequency cloud, and top-emoji pie chart from local text exports.

====================================Overview------------------------------------------------------------------
Analyze exported WhatsApp chats in the browser with interactive stats, charts, and tables built using Streamlit, Matplotlib, and Seaborn. The app supports overall and per-user breakdowns, including message counts, word counts, media/link counts, busiest users, wordclouds, and emoji distributions.

----------------------------------------------Features----------------------------------------------------

Upload WhatsApp .txt exports and auto-parse to a clean DataFrame for analysis.

Top statistics: total messages, words, media messages, and links for overall or a selected participant.

“Most Busy” participant view with a bar chart and contribution table when analyzing overall chats.

Wordcloud visualization of frequent words for overall or per-user selection.

Emoji analysis with a table of counts and a pie chart of top emojis (with emoji font rendering).


-------------------------------Project_Structure-----------------------------------------------------
Project Structure
app.py — Streamlit UI, charts, and layout.

preprocessor.py — parsing and cleaning WhatsApp text exports into a DataFrame.

helper.py — statistics, busy-user computation, wordcloud generation, emoji extraction.

requirements.txt — Python dependencies for reproducible setup.



-------------------------------------------Getting Started----------------------------------
Clone the repository and install dependencies:

python -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate

pip install -r requirements.txt

Run the app:

streamlit run app.py, then open the local URL shown in the terminal.

---------------------------------Exporting WhatsApp Chats-------------------------------------------------------------

Open the desired chat (individual or group), choose Export Chat, select Without Media, and save the .txt file for upload to the app.

For large chats, export may take time; keep the app window open during upload and parsing.




---------------------------------------Tech Stack------------------------------------------------------------------

Streamlit for UI, Matplotlib/Seaborn for plotting, and Python for preprocessing and analysis utilities.

-------------------------------------------Contributing--------------------------------------------------------------


Issues and pull requests are welcome. Consider adding tests, sample chat files (anonymized), or new visualizations as described in the Features section.

-------------------------------------------------License-------------------------------------------------------------


Add a LICENSE file (for example, MIT or Apache-2.0). See choosealicense.com for guidance.

--------------------------------------------Acknowledgements----------------------------------------------------------------


Thanks to the open-source community for guides and best practices on writing clear READMEs and effective Streamlit apps.




