#!/usr/bin/env python3
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        recipient_email = 'haydandebonis@outlook.com'
        
        msg = MIMEMultipart()
        msg['From'] = 'noreply@thefidgetshop.com'
        msg['To'] = recipient_email
        msg['Subject'] = f'Contact Form Message from {name}'
        
        body = f"""
New contact form submission:

Name: {name}
Email: {email}

Message:
{message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('SMTP_PORT', '587'))
        smtp_user = os.getenv('SMTP_USER', '')
        smtp_password = os.getenv('SMTP_PASSWORD', '')
        
        if not smtp_user or not smtp_password:
            return jsonify({
                'status': 'error',
                'message': 'Email service not configured. Please contact us at haydandebonis@outlook.com directly.'
            }), 503
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        text = msg.as_string()
        server.sendmail(msg['From'], recipient_email, text)
        server.quit()
        
        return jsonify({'status': 'success', 'message': 'Email sent successfully'}), 200
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': f'Failed to send email. Please contact us at haydandebonis@outlook.com directly.'
        }), 500

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
