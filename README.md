# Summail – AI-Powered Email Summarizer and Priority Sorter

## Project Overview

Summail is a web-based AI application designed to simplify email management. It securely connects to a user's Gmail account using the Gmail API, fetches recent emails, and uses Natural Language Processing (NLP) techniques to generate concise summaries. The system also classifies emails into High, Medium, and Low priority categories, enabling users to quickly identify and focus on the most important messages.

---

## Key Features

* Secure Gmail authentication using OAuth 2.0
* AI-powered email summarization
* Intelligent email priority classification
* Automated email processing
* User-friendly web interface
* Real-time email retrieval and analysis

---

## Technology Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### APIs and Libraries

* Gmail API
* Hugging Face Transformers
* NLTK
* Google Authentication Libraries

---

## System Requirements

* Python 3.7 or above
* Gmail account
* Internet connection
* Google Cloud Project with Gmail API enabled

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Summail.git
cd Summail
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gmail API

1. Open Google Cloud Console
2. Create a new project
3. Enable Gmail API
4. Configure the OAuth Consent Screen
5. Create OAuth 2.0 Credentials
6. Download the `credentials.json` file
7. Place `credentials.json` in the project root directory

### 5. Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://localhost:5000
```

---

## How It Works

1. The user signs in securely using Gmail OAuth.
2. The Gmail API retrieves recent emails.
3. Email content is processed using Hugging Face Transformer models.
4. AI generates concise summaries of the emails.
5. Emails are categorized into High, Medium, or Low priority.
6. The summarized and prioritized emails are displayed through a clean web interface.

---

## Project Structure

```text
Summail/
│
├── templates/
│   ├── inbox.html
│   ├── summary.html
│   ├── welcome.html
│   └── email_detail.html
│
├── static/
├── uploads/
├── data/
├── models/
│
├── app.py
├── gmail_auth.py
├── summarizer.py
├── credentials.json
├── requirements.txt
├── Procfile
└── token.pickle
```

---

## Usage Tips

* Ensure that the `credentials.json` file is placed correctly.
* Verify that Gmail API is enabled in Google Cloud Console.
* The summarization process may take a few seconds depending on internet speed and model loading time.
* Use a modern browser for the best experience.

---

## Common Issues and Solutions

### OAuth Error: Redirect URI Mismatch

Verify the authorized redirect URIs configured in Google Cloud Console.

### Email Summaries Not Generated

* Check internet connectivity
* Verify model availability
* Ensure all required packages are installed

### Authentication Issues

Delete the existing token file and authenticate again.

---

## Future Enhancements

* Support for multiple email accounts
* Customizable summary lengths
* Email scheduling and reply assistance
* Mobile-responsive interface
* Integration with Outlook and other email platforms
* Advanced AI-based categorization and recommendations

---

## Applications

* Email productivity management
* Corporate communication analysis
* Student and professional email organization
* Intelligent inbox management
* AI-assisted information extraction

---

## License

This project is developed for educational and academic purposes only and is not intended for commercial use.

---

## Authors

Bhavya Sree and Team

