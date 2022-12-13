import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5767994238:AAEDtTLRRWUOJL3TgnHHdJ9Xz2Poa19LnOs")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6216349"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5c7418e9f3df6db931caa7354521c55f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001840341492"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1289438071"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://tbfroqwjtwdgue:e57d95aa075eff7ed7bc4c2d7ca24aac187f26e06ebff002855bc7f6cae0bf02@ec2-52-204-46-21.compute-1.amazonaws.com:5432/d5kdoihgi0ife0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001465375204"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001436285912"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "{first} Kamu Harus Join Channel Dan Grup Terlebih Dahulu Ya Sebelum Melihat File Video ini.\n\nTutorial :\n-[1.  Klik Start Bot\n-[2. Join Channel & Group⬇️\n-[3. Try Again dan Start-\n[4. Tunggu hingga Video nya Muncul\n-[5. Selamat Menikmati Asupan nya\nNote :\nJangan spam ya karna bisa membuat bot delayed.\nSekian dan Terima Kasih.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5555532485 904692453").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
