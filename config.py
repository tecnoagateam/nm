# Don't ask me why this looks like a fucking shit! Just go and make a fukcking PR as i'm fucking lazy to do these things! Fuck Off!

import os
from os import getenv

from pyrogram import Client
from dotenv import load_dotenv
from helpers.modhelps import fetch_heroku_git_url

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "AgClBHUsSGWhIN-lgq5LuPS3NZPOI2q-dwRHF6DMzVdRfm5yBzLcJqXSlEZdf0iLIMFcC2YVEr9M1hFc2vx2QKxRgSvhCSSu79YeY_H7qJ4vz_ScnoIjs2kmGVd6RcUERrCNECQvyhk_qZiqjgk5n3JNzQNUPztt5ynK-HbHYwQx8tF3DdQPFI-mRIfzJnsdoTGMX_Yin7cG7XjF-nXV5tmEFPL0scIl_VCrVm4Ezgm8d9U9ThMoga-Ptxhl1hlSQvQNThdioVbVN3cMhC9QC_0278J8GCqy2EyOi_w2CkImQznsQpchozdSeONHrZwCmBi_tkZzVGnV9yHqrd-wM660Wp7lFQA")
BOT_TOKEN = getenv("BOT_TOKEN", "6254171749:AAFn9tbZaVK4nTuhAbYX6mVqzVPYpJ-YdNk")

API_ID = int(getenv("API_ID", "18052289"))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "35"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

# Your Telegram User ID
BOT_OWNER = int(os.environ.get("BOT_OWNER", "1924693109"))
# Sudo users IDs, They are admins everywhere
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1924693109").split()))
# Your Bot's Username without "@"
BOT_USERNAME = os.environ.get("BOT_USERNAME", "nilaymusicbot")
# Your MongoDB url
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://nilay:nilay2004@nilay.kavmyqy.mongodb.net/?retryWrites=true&w=majority")
# Your Log Channel! Make a private channel and get it's ID
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001679945097"))
# If you need to broadcast messages as a copy or Forwarded Message
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
# Thumbnail URL
THUMB_URL = os.environ.get("THUMB_URL", "https://telegra.ph/file/2ed47c81eda6b0624021d.jpg")
# Your Updates Channel! Don't Put Anything If you don't have one
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "ledyplaylist")

# Your ARQ API Key
ARQ_API_KEY = getenv("ARQ_API_KEY")
# Don't Change Anything Here
ARQ_API_URL = "https://grambuilders.tech/"

# Updator Configs
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/tecnoagateam/nm")
U_BRANCH = "master"
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

# Versions
cp_version = "v2.9.3.2"
nexaub_version = "v0.4"
