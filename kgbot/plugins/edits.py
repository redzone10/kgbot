import asyncio
from collections import deque

from kgbot import CMD_HELP
from kgbot.utils import admin_cmd


@kgbot.on(admin_cmd(pattern=r"candy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐ฆ๐ง๐ฉ๐ช๐๐ฐ๐ง๐ซ๐ฌ๐ญ"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@kgbot.on(admin_cmd(pattern=r"nothappy"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐โน๏ธ๐โน๏ธ๐โน๏ธ๐"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@kgbot.on(admin_cmd(pattern=r"heart"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("โค๏ธ๐งก๐๐๐๐๐ค"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@kgbot.on(admin_cmd(pattern=r"tlol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐ค๐ง๐คจ๐ค๐ง๐คจ"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@kgbot.on(admin_cmd(pattern=r"lol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("๐๐คฃ๐๐คฃ๐๐คฃ"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)


@kgbot.on(admin_cmd(pattern=r"lmoon"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 32)
    await event.edit("moon")
    animation_chars = [
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
        "๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐\n๐๐๐๐๐",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@kgbot.on(admin_cmd(pattern=r"moon"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 33)
    await event.edit("moon")
    animation_chars = [
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 33])


CMD_HELP.update(
    {
        "edits": "โ `.lol` \n `.candy` \n `.nothappy` \n `.heart` \n `.tlol` \nUse - Try Yourself\n `.moon` \nUse- Moon\n `.lmoon` \nUse- Long Moon"
    }
)
