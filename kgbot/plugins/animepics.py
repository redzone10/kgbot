import json
import os
import urllib

import requests

from kgbot import CMD_HELP
from kgbot.utils import admin_cmd


@kgbot.on(admin_cmd(pattern="animepic"))
async def _(event):
    if event.fwd_from:
        return
    with urllib.request.urlopen("https://api.waifu.pics/sfw/waifu") as url:
        data = json.loads(url.read().decode())
    finalcat = data["url"]
    r = requests.get(finalcat, allow_redirects=True)
    open("animepicthunder.jpg", "wb").write(r.content)
    await kgbot.send_file(
        event.chat_id,
        "animepicthunder.jpg",
        caption=f"Here's Your Waifu..\nGathered By Your @kgbot",
    )
    os.system("rm animepicthunder.jpg")


CMD_HELP.update({"animepics": "➟ `.animepic \nUse - Get Random Waifu Images"})
