from kgbot import CMD_HELP
from kgbot.utils import admin_cmd


@kgbot.on(admin_cmd("duckduckgo (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ", "+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.edit(
            "Let Me 🦆 DuckDuckGo That For From My kgbot⚡️:\n🔎 [{}]({})".format(
                input_str, link
            )
        )
    else:
        await event.edit("something is wrong. please try again later.")


CMD_HELP.update(
    {"duckduckgo": ".duckduckgo\nUse - To Get Direct Search Link To Duckduckgo."}
)
