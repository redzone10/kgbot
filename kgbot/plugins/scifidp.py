import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from kgbot import CMD_HELP
from kgbot.utils import admin_cmd

COLLECTION_STRING = [
    "star-wars-wallpaper-1080p",
    "4k-sci-fi-wallpaper",
    "star-wars-iphone-6-wallpaper",
    "kylo-ren-wallpaper",
    "darth-vader-wallpaper",
]


async def scifipp():

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    plist = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(plist)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/kgproject1010/kgbot/raw/master/Extras/kgproject1010font.ttf",
            "f.ttf",
        )

    r = requests.get(fy, allow_redirects=True)
    open("kgbotautopic.jpg", "wb").write(r.content)


@kgbot.on(admin_cmd(pattern="scidp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Automatic Sci-Fi Profile Pic**.\n`Please Note That It Will Automatically Update Your Profile Pic After 10 Minutes`\nBy Your[kgbot](https://github.com/kgproject1010/kgbot)"
    )

    while True:

        await scifipp()
        file = await event.client.upload_file("kgbotautopic.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf kgbotautopic.jpg")
        await asyncio.sleep(600)


CMD_HELP.update({"scifidp": ".scifidp\nUse - Autochanging Sci-Fi Profile Pic."})
