# Copyright (C) 2022 CtrlUB
#
# This file is a part of < https://github.com/kennedy-ex/CtrlUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/kennedy-ex/CtrlUB/blob/main/LICENSE/>.
#


import sys
import importlib
from pyrogram import idle
from uvloop import install
from CtrlUB.config import BOT_TOKEN

from CtrlUB.version import __version__ as botver
from CtrlUB import *
from CtrlUB.helpers.misc import heroku, git
from CtrlUB.logging import LOGGER


MSG_ON = """
✅ **CtrlUB Is Actived!**
➠ **Userbot Version -** `{}`
➠ **Try** `alive` **for check your bot**
"""


async def main():
    if bot:
        await bot.start()
        getbot = await bot.get_me()
        LOGGER("Assistant Bot").info(f"Started as {getbot.first_name} [{getbot.id}]")
    await app.start()
    get1 = await app.get_me()
    try:
        await app.join_chat("gcaika")
        await app.send_message(
            BOTLOG_CHATID,
            MSG_ON.format(botver)
        )
    except:
        LOGGER("BOTLOG_CHATID").info(f"Can't acces by client 1 or not configured.")
        pass
    LOGGER("Client 1").info(f"Started as {get1.first_name} [{get1.id}]")
    if app2:
        await app2.start()
        get2 = await app2.get_me()
        try:
            await app2.join_chat("gcaika")
            await app2.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            LOGGER("BOTLOG_CHATID").info(f"Can't acces by client 2 or not configured.")
            pass
        LOGGER("Client 2").info(f"Started as {get2.first_name} [{get2.id}]")
    if app3:
        await app3.start()
        get3 = await app3.get_me()
        try:
            await app3.join_chat("gcaika")
            await app3.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            LOGGER("BOTLOG_CHATID").info(f"Can't acces by client 3 or not configured.")
            pass
        LOGGER("Client 3").info(f"Started as {get3.first_name} [{get3.id}]")
    if app4:
        await app4.start()
        get4 = await app4.get_me()
        try:
            await app4.join_chat("gcaika")
            await app4.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            LOGGER("BOTLOG_CHATID").info(f"Can't acces by client 4 or not configured.")
            pass
        LOGGER("Client 4").info(f"Started as {get4.first_name} [{get4.id}]")
    if app5:
        await app5.start()
        get5 = await app5.get_me()
        try:
            await app5.join_chat("gcaika")
            await app5.send_message(
                BOTLOG_CHATID,
                MSG_ON.format(botver)
            )
        except:
            LOGGER("BOTLOG_CHATID").info(f"Can't acces by client 5 or not configured.")
            pass
        LOGGER("Client 5").info(f"Started as {get5.first_name} [{get5.id}]")
    LOGGER("CtrlUB").info(f"Bot v{botver} is actived!")
    await idle()
    await aiosession.close()

if __name__ == "__main__":
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
