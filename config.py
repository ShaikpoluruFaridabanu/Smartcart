"""SmartCart configuration. Set these values in environment variables.

Never commit real passwords or Razorpay secrets to source control.
"""
SECRET_KEY = "your_secret_key"

# MySQL Database
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "smartcart_db"

# Email SMTP Settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'wajidpro131@gmail.com'
MAIL_PASSWORD = 'jrna ahpk rkou ngtg'   # Gmail App Password

#razor pay
RAZORPAY_KEY_ID = "rzp_test_TvefaOS7vEHSZs"
RAZORPAY_KEY_SECRET = "PNZEvxHNCjTmEXkSSrTTVA8B"