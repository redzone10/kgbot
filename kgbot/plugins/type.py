import asyncio

from kgbot import CMD_HELP
from kgbot.utils import admin_cmd


@kgbot.on(admin_cmd(pattern="type (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    ohkekekeke = "\u2060"
    for i in range(601):
        ohkekekeke += "\u2060"
    try:
        await event.edit(shiiinabot)
    except Exception as e:
        logger.warn(str(e))
    typing_symbol = "|"
    DELAY_BETWEEN_EDITS = 0.3
    previous_text = ""
    await event.edit(typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        try:
            await event.edit(typing_text)
        except Exception as e:
            logger.warn(str(e))
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        try:
            await event.edit(previous_text)
        except Exception as e:
            logger.warn(str(e))
        await asyncio.sleep(DELAY_BETWEEN_EDITS)


CMD_HELP.update({"type": "➟ `.type <your message>` \nUse - Type Type Type"})
