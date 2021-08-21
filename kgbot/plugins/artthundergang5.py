"""Plugin made by kgproject1010 for kgbot 
and if you will copy it without credits then you are the biggest gay of this universe"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from kgbot.utils import admin_cmd

Z = ("░▄░█░░░▄▀▀▀▀▀▄░░░█░▄░\n"
"▄▄▀▄░░░█─▀─▀─█░░░▄▀▄▄\n"
"░░░░▀▄▒▒▒▒▒▒▒▒▒▄▀░░░░\n"
"░░░░░█────▀────█░░░░░\n"
"░░░░░█────▀────█░░░░░\n")
X = ("░░░░░░░░░░░░░░░░▄▓▄\n"
"░░░░▄█▄░░░░░░░░▄▓▓▓▄\n"
"░░▄█████▄░░░░░▄▓▓▓▓▓▄\n"
"░▀██┼█┼██▀░░░▄▓▓▓▓▓▓▓▄\n"
"▄▄███████▄▄▄▄▄▄▄▄█▄▄▄▄\n")
C = ("░▄▀▀▀▀▄░░▄▄\n"
"█░░░░░░▀▀░░█░░░░░░▄░▄\n"
"█░║░░░░██░████████████ \n"
"█░░░░░░▄▄░░█░░░░░░▀░▀\n"
"░▀▄▄▄▄▀░░▀▀\n")
V = ("░▄▌░░░░░░░░░▄\n"
"████████████▄\n"
"░░░░░░░░▀▐████\n"
"░░░░░░░░░░░▐██▌\n")
B = ("─────▀▄▀─────▄─────▄\n"
"──▄███████▄──▀██▄██▀\n"
"▄█████▀█████▄──▄█\n"
"███████▀████████▀\n"
"─▄▄▄▄▄▄███████▀\n")

@kgbot.on(admin_cmd(pattern=r"snowman"))
async def nandysnowman(snowman):
    await snowman.edit(Z)
@kgbot.on(admin_cmd(pattern=r"home"))
async def nandyhome(home):
    await home.edit(X)
@kgbot.on(admin_cmd(pattern=r"guitar"))
async def nandyguitar(guitar):
    await guitar.edit(C)
@kgbot.on(admin_cmd(pattern=r"pistol"))
async def nandypistol(pistol):
    await pistol.edit(V)
@kgbot.on(admin_cmd(pattern=r"whale"))
async def nandywhale(whale):
    await whale.edit(B)
