import asyncio
import os
import random
import re
import urllib
import requests
from telethon.tl import functions
from kgbot import CMD_HELP

COLLECTION_STRING = [
    "cool-cat-wallpaper",
    "1920x1080-cat-wallpaper",
    "cat-wallpapers-and-screensavers",
    "baby-cat-wallpaper",
    "funny-cat-desktop-wallpaper",
]


async def meowkgproject1010():


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
    open('kgbotautopic.jpg', 'wb').write(r.content)


@kgbot.on(admin_cmd(pattern="meowpfp"))
async def main(event):

    await event.edit(
        "**Starting Automatic Cats Profile Pic**.\n`Please Note That It Will Automatically Update Your Profile Pic After 10 Minutes`\nBy Your[kgbot](https://github.com/kgproject1010/kgbot)"
    )

    while True:

        await meowkgproject1010()
        file = await event.client.upload_file("kgbotautopic.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf kgbotautopic.jpg")
        await asyncio.sleep(600)  


CMD_HELP.update(
    {"catsautopic": "➟ `.meowpfp`\nSelects Randomly A Cute Cat Pic And Sets As Your Profile Picture.."}
)
