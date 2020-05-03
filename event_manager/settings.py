import django.conf.global_settings as settings
from azure.storage.blob import BlobServiceClient
from corsheaders.defaults import default_headers
import socket

from .default_settings import *


AUTH_USER_MODEL = "event_app.User"

AUTHENTICATION_BACKENDS = settings.AUTHENTICATION_BACKENDS + [
    "event_app.backend.AuthBackend"
]


STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = list(default_headers) + ["Token"]

if DEBUG:
    PROFILECONTAINER = "eventmanagerprofiledebug"
    ICONCONTAINER = "eventmanagericondebug"
else:
    PROFILECONTAINER = "eventmanagerprofile"
    ICONCONTAINER = "eventmanagericon"

STORAGE_CLIENT = BlobServiceClient.from_connection_string(
    os.getenv("CONNECTION_STRING")
)

RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")
RAZORPAY_KEY = os.getenv("RAZORPAY_KEY")
PAYMENT_CALLBACK_URL = os.getenv('PAYMENT_CALLBACK_URL')
PAYMENT_REDIRECT_URL = os.getenv('PAYMENT_REDIRECT_URL')
PAYMENT_TEST = int(os.getenv('PAYMENT_TEST')) == 1

if DEBUG:
    ADMINS = ['shohanduttaroy99@gmail.com']
else:
    ADMINS = ['shohanduttaroy99@gmail.com', 'prasadyash549@yahoo.com', 'akashsurana119@gmail.com']

EMAIL_HOST = socket.gethostbyname('mail.privateemail.com')
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
