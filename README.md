Summail – AI-Powered Email Summarizer and Priority Sorter 
Project Overview: 
Summail is a web-based AI application designed to simplify the management of emails. 
It connects securely to a user’s Gmail account using the Gmail API, fetches recent 
emails, and uses Natural Language Processing techniques to summarize them concisely. 
It also classifies these emails based on their importance into high, medium, and low 
priority categories. This allows users to quickly understand the content of their emails 
and focus on the most important ones. 
Key Features: 
The project offers several features including secure Gmail login via OAuth 2.0, AI
powered email summarization using transformer models, intelligent email priority 
sorting, a user-friendly interface built with Flask, and automated processing of emails. 
Technology Stack: 
The backend is developed in Python using the Flask framework. The frontend is built 
with HTML, CSS, and JavaScript. Key APIs and libraries used include the Gmail API for 
fetching emails and Hugging Face Transformers for summarization. 
System Requirements: 
To run the project, you need Python 3.7 or above, a Gmail account, an internet 
connection, and a configured Google Cloud project with the Gmail API enabled. 
Installation and Setup: 
First, clone the project repository. Then, optionally create and activate a virtual 
environment. Next, install all required Python packages using pip. After that, set up 
Gmail API credentials by creating a project in Google Cloud Console, enabling the Gmail 
API, configuring the OAuth consent screen, creating OAuth 2.0 credentials, and 
downloading the credentials.json file. Place this file in the project directory. Finally, run 
the Flask application and open it in a browser at http://localhost:5000. 
How It Works: 
After the user logs in with Gmail, the application fetches emails using the Gmail API. 
Each email is summarized using an NLP model from Hugging Face. Then, the system 
classifies each email into a priority category based on its content and subject. The 
summarized and sorted emails are displayed in a clean web interface. 
Project Structure: 
The main folders include templates for HTML files, static for CSS and JavaScript, and 
Python files such as app.py and summarizer.py. The credentials.json file is used for 
Gmail API authentication and requirements.txt contains the list of dependencies. 
Usage Tips: 
Ensure that the credentials.json file is placed correctly and contains valid keys. The 
application may take a few seconds to load summaries depending on internet speed. Use 
a modern browser for the best experience. 
Common Issues and Solutions: 
OAuth errors like redirect URI mismatch should be resolved by checking the Google 
Cloud configuration. If summaries are not generated, check internet connectivity and 
model availability. Make sure Flask and other dependencies are installed correctly. 
Future Enhancements: 
Planned improvements include support for multiple accounts, customizable summaries, 
local storage of summaries, email reply and scheduling features, mobile responsiveness, 
and integration with other email platforms like Outlook. 
License: 
This project is created for educational and academic purposes only and is not intended for 
commercial use. 
Developed By: 
Kothapalli Sowmya(23251A05M0) 
Bandapalli Bhavya Sree(23251A05P1) 
Cheguri Khethana(24255A0526)
