import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

# Email credentials
SMTP_SERVER = 'smtp.gmail.com'  # Gmail SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'andyspacex10@gmail.com'  # Your email address
EMAIL_PASSWORD = 'Qwerty42055'  # Your email app password

# Replace with your email address to receive messages
RECIPIENT_EMAIL = 'andyspacex10@gmail.com'


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message_body = data.get('message', '')

    if not message_body:
        return jsonify({'status': 'No message provided'}), 400

    try:
        # Create the email content
        msg = MIMEText(message_body)
        msg['Subject'] = 'New Message from Website'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to email account
            server.send_message(msg)  # Send the email

        return jsonify({'status': 'Email sent'}), 200
    except Exception as e:
        return jsonify({'status': 'Failed to send email', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
