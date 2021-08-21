import os
import sys
from kgbot import CMD_HELP, CMD_HNDLR
from kgbot.utils import admin_cmd


@kgbot.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        f"**Restarting Your kgbot**.. Please Wait Until It Starts Again "
    )
    await kgbot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

CMD_HELP.update(
    {
        "restart": ".restart\nUse - Restarts the bot."
    }
)
