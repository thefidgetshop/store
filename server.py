#!/usr/bin/env python3
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import json

app = Flask(__name__, static_folder='.')
app.secret_key = os.environ.get("SESSION_SECRET", "fidget-shop-secret-key-change-in-production")
CORS(app)

ADMIN_USERS = {
    'rory': 'thefidgshop',
    'haydan': 'thefidgshop',
    'temp': 'thefidgshop'
}

def get_db_connection():
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    return conn

def check_admin_auth():
    auth = request.headers.get('Authorization')
    if not auth or not auth.startswith('Basic '):
        return False
    
    try:
        import base64
        credentials = base64.b64decode(auth.split(' ')[1]).decode('utf-8')
        username, password = credentials.split(':', 1)
        return username in ADMIN_USERS and ADMIN_USERS[username] == password
    except:
        return False

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

@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        
        if not data.get('email'):
            return jsonify({'status': 'error', 'message': 'Email is required'}), 400
        
        delivery_method = data.get('deliveryMethod')
        payment_method = data.get('paymentMethod')
        
        if delivery_method == 'shipping':
            required_fields = ['fullName', 'address', 'city', 'state', 'zipCode']
            if not all([data.get(field) for field in required_fields]):
                return jsonify({'status': 'error', 'message': 'Complete shipping address is required for delivery'}), 400
        
        if payment_method == 'card':
            required_fields = ['cardNumber', 'expiry', 'cvv']
            if not all([data.get(field) for field in required_fields]):
                return jsonify({'status': 'error', 'message': 'Complete card information is required for card payment'}), 400
        
        if payment_method == 'cash' and delivery_method != 'pickup':
            return jsonify({'status': 'error', 'message': 'Cash payment requires local pickup'}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO orders (full_name, email, address, city, state, zip_code, 
                              delivery_method, payment_method, subtotal, shipping, total, items)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            data.get('fullName'),
            data.get('email'),
            data.get('address'),
            data.get('city'),
            data.get('state'),
            data.get('zipCode'),
            data.get('deliveryMethod'),
            data.get('paymentMethod'),
            data.get('subtotal'),
            data.get('shipping'),
            data.get('total'),
            json.dumps(data.get('items', []))
        ))
        
        order_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'status': 'success', 'orderId': order_id}), 201
        
    except Exception as e:
        print(f"Error creating order: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/orders', methods=['GET'])
def get_orders():
    if not check_admin_auth():
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401
    
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("""
            SELECT id, full_name, email, address, city, state, zip_code,
                   delivery_method, payment_method, subtotal, shipping, total,
                   items, created_at
            FROM orders
            ORDER BY created_at DESC
        """)
        
        orders = cur.fetchall()
        cur.close()
        conn.close()
        
        orders_list = []
        for order in orders:
            order_dict = dict(order)
            order_dict['timestamp'] = order_dict['created_at'].isoformat() if order_dict.get('created_at') else None
            del order_dict['created_at']
            orders_list.append(order_dict)
        
        return jsonify(orders_list), 200
        
    except Exception as e:
        print(f"Error fetching orders: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/contact', methods=['POST'])
def create_contact_message():
    try:
        data = request.json
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO contact_messages (name, email, message)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (
            data.get('name'),
            data.get('email'),
            data.get('message')
        ))
        
        message_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'status': 'success', 'messageId': message_id}), 201
        
    except Exception as e:
        print(f"Error creating contact message: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/contact', methods=['GET'])
def get_contact_messages():
    if not check_admin_auth():
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401
    
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("""
            SELECT id, name, email, message, created_at
            FROM contact_messages
            ORDER BY created_at DESC
        """)
        
        messages = cur.fetchall()
        cur.close()
        conn.close()
        
        messages_list = []
        for msg in messages:
            msg_dict = dict(msg)
            msg_dict['timestamp'] = msg_dict['created_at'].isoformat() if msg_dict.get('created_at') else None
            del msg_dict['created_at']
            messages_list.append(msg_dict)
        
        return jsonify(messages_list), 200
        
    except Exception as e:
        print(f"Error fetching contact messages: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
