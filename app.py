from flask import Flask, render_template, request, redirect, url_for
from gmail_auth import authenticate_gmail, fetch_emails, get_email_by_id
from summarizer import generate_summary
import os
import warnings
warnings.filterwarnings('ignore', category=UserWarning)

app = Flask(__name__)

# Global store for emails and priority categories
emails_data = []
high_priority = []
medium_priority = []
low_priority = []
spam = []

# Priority Keywords (You can customize these)
URGENT_KEYWORDS = ["urgent", "important", "action required", "critical"]
SPAM_KEYWORDS = ["advertisement", "offer", "discount", "subscribe"]
HIGH_PRIORITY_SENDERS = ["boss@company.com", "support@important.com"]  # Example

def assess_priority(email):
    subject = email['subject'].lower()
    body = email['body'].lower()
    sender = email['sender'].lower()

    if any(keyword in subject or keyword in body for keyword in SPAM_KEYWORDS) or "unsubscribe" in body:
        return "spam"

    if any(keyword in subject or keyword in body for keyword in URGENT_KEYWORDS) or sender in HIGH_PRIORITY_SENDERS:
        return "high"

    if len(subject) < 5:  # Short subject, potentially less important
        return "low"

    return "medium"

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/inbox')
def inbox():
    global emails_data, high_priority, medium_priority, low_priority, spam
    service = authenticate_gmail()
    emails_data = fetch_emails(service, max_results=50)  # Show up to 50 emails

    # Clear priority lists before re-populating
    high_priority.clear()
    medium_priority.clear()
    low_priority.clear()
    spam.clear()

    # Assess and categorize emails
    for email in emails_data:
        priority = assess_priority(email)
        if priority == "high":
            high_priority.append(email)
        elif priority == "medium":
            medium_priority.append(email)
        elif priority == "low":
            low_priority.append(email)
        elif priority == "spam":
            
            spam.append(email)

    return render_template('inbox.html',
                           high_priority=high_priority,
                           medium_priority=medium_priority,
                           low_priority=low_priority,
                           spam=spam)

@app.route('/email/<id>')
def email_detail(id):
    global emails_data
    email = next((e for e in emails_data if e['id'] == id), None)
    if not email:
        return "Email not found", 404
    return render_template('email_detail.html', email=email)

@app.route('/summary/<id>')
def email_summary(id):
    global emails_data
    email = next((e for e in emails_data if e['id'] == id), None)
    if not email:
        return "Email not found", 404
    summary = generate_summary(email['body'])
    return render_template('summary.html', email=email, summary=summary)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    filtered = [email for email in emails_data if query.lower() in email['subject'].lower() or query.lower() in email['sender'].lower()]
    return render_template('inbox.html',
                           high_priority=[email for email in filtered if assess_priority(email) == "high"],
                           medium_priority=[email for email in filtered if assess_priority(email) == "medium"],
                           low_priority=[email for email in filtered if assess_priority(email) == "low"],
                           spam=[email for email in filtered if assess_priority(email) == "spam"])

if __name__ == '__main__':
    app.run(debug=True)