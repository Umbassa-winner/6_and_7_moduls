import os
from dotenv import load_dotenv

load_dotenv()

class CommonUserCreds:
    EMAIL = os.getenv("EMAIL_REGISTERED_USER")
    PASSWORD = os.getenv("PASSWORD_REGISTERED_USER")

