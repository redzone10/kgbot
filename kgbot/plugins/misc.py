import asyncio
from telethon import events
from kgbot.utils import admin_cmd
from kgbot import CMD_HELP

@kgbot.on(admin_cmd("support"))
async def support(event):
    if event.fwd_from:
        return
    await event.edit(
        "⚡**kgbot**⚡\n"
        "•[Channel](https://t.me/rakasupport)\n"
        "•[Support Group](https://t.me/KGSupporrgroup)\n"
        "•[Owner](https://t.me/kgbot)\n"
)

@kgbot.on(admin_cmd("docs"))
async def docs(event):
    await event.edit(
        "⚡**kgbot**⚡\n"
        "•[Docs](https://kgproject1010.gitbook.io/kgbot/)\n"
        "•[Youtube Tutorial](https://youtu.be/7530SjgsgW4)\n"
        "•[Repo](https://github.com/kgproject1010/kgbot)\n"
)

CMD_HELP.update(
    {
        "misc": " `.support` \
\nUse - : Support.\
\n\n `.docs` \
\nUse - : Docs."
    }
)
