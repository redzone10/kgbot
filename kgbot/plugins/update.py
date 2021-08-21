import os
import sys

from kgbot import CMD_HELP
from kgbot.utils import admin_cmd


@kgbot.on(admin_cmd(pattern="update"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        f" ⚡️⚡️**Updating Your kgbot**⚡️⚡️ ... \n\nPlease Wait Until It Starts Again✅\nFor More, Get Help From [Here](https://t.me/kgbot) "
    )
    await kgbot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


CMD_HELP.update({"update": "`.update`\nUse - Updates Your kgbot."})
