import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request

# Create logs directory if it doesn't exist
log_dir = os.path.abspath(os.path.dirname(__file__))
log_file_path = os.path.join(log_dir, 'http_audits.log')

# Setup logger
logging_format = logging.Formatter('%(asctime)s %(message)s')
f_logger = logging.getLogger('HTTP_logger')
f_logger.setLevel(logging.INFO)

f_handler = RotatingFileHandler(log_file_path, maxBytes=5000, backupCount=3)
f_handler.setFormatter(logging_format)
f_logger.addHandler(f_handler)

# Web honeypot
def web_honeypot(input_username="admin", input_password="password"):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('admin.html')  # Ensure templates/admin.html exists

    @app.route('/wp-admin-login', methods=['POST'])
    def login():
        try:
            username = request.form['username']
            password = request.form['password']
            ip_address = request.remote_addr

            log_msg = f'Client IP: {ip_address} | Username: {username} | Password: {password}'
            f_logger.info(log_msg)
            print(log_msg, flush=True)  # Also print for quick testing

            if username == input_username and password == input_password:
                return 'Successfully Logged In'
            else:
                return 'Invalid Username or Password. Please Try Again.'
        except Exception as e:
            f_logger.error(f"Error processing login: {str(e)}", exc_info=True)
            return "Internal Server Error", 500

    return app

def run_web_honeypot(port=2903, input_username="admin", input_password="password"):
    app = web_honeypot(input_username, input_password)
    app.run(debug=False, port=port, host="0.0.0.0")

# Run honeypot
if __name__ == '__main__':
    run_web_honeypot(port=2903)
