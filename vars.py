#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "19979002"))
API_HASH = environ.get("API_HASH", "200505dafbb32ed69aefefc013c3939d")
BOT_TOKEN = environ.get("BOT_TOKEN", "8091183324:AAHQ3c8TOR_A-O8Bn_URzNolGg-vq_uxSRs")
OWNER = int(environ.get("OWNER", "6378469891"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
