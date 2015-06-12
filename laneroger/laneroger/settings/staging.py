from .base import *

# UPDATE HERE: The below ALLOWED_HOSTS must contain the nginx server_url,
#              otherwise, you'll get a BAD REQUEST ERROR
ALLOWED_HOSTS = ['laneroger.na-inter.net', '127.0.0.1', ]

# ######### EMAIL CONFIGURATION
# djrill
MANDRILL_API_KEY = "RLMV5rUKNHd6tBTCknmVLA"  # roger@na-inter.net API Key
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
SERVER_EMAIL = 'Elaine & Roger <roger@na-inter.net>'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
