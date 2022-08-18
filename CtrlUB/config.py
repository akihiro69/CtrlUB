# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB-Userbot/blob/main/LICENSE/>.
#


from base64 import b64decode as kk
from distutils.util import strtobool
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = [
    -1001473548283,
    -1001606516367,
    -1001459812644,
    -1001578091827,
    -1001748391597,
]
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", or 0))
BRANCH = getenv("BRANCH", "main")
DB_URL = getenv("DATABASE_URL", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
TOKEN = getenv(
    "TOKEN",
    kk("Z2hwX3NnWG5DSGZVNmRiek9IZkFwZHhFbzY0a2VzM2VRWjNmNkxpdg==")
        .decode("utf-8")
)
STRING_SESSION = getenv("STRING_SESSION", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
