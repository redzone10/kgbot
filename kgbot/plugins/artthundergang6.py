"""Plugin made by kgproject1010 for kgbot 
and if you will copy it without credits then you are the biggest gay of this universe"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from kgbot.utils import admin_cmd

N = ("▄▀─────────────▀▄\n"
"█▄█──█▀█─█▀█─▄█▄█\n"
"─▀██▄▀▄▀─▀▄▀▄██▀\n"
"░░░▄██▀███▀███▄\n"
"░▐▀█▀██▄▄▄██▀█▀▌\n")
M = ("║░█░█░║░█░█░█░║░█░█░║\n"
"║░█░█░║░█░█░█░║░█░█░║\n"
"║░║░║░║░║░║░║░║░║░║░║\n"
"╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝\n")
QQ = ("───────▄██████▄───────\n"
"──────▐▀▀▀▀▀▀▀▀▌──────\n"
"──────▌▌▀▀▌▐▀▀▐▐──────\n"
"──────▐──▄▄▄▄──▌──────\n"
"───────▌▐▌──▐▌▐───────\n")
WW = ("───▄▀▀▀▀▀───▄█▀▀▀█▄\n"
"──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██\n"
"──▐▒▒▒▒▒▒▒▒███▌▀▐███\n"
"───▌▒▓▒▒▒▒▓▒██▌▀▐██\n"
"───▌▓▐▀▀▀▀▌▓─▀▀▀▀▀\n")
EE = ("──███▅▄▄▄▄▄▄▄▄▄\n"
"─██▐████████████\n"
"▐█▀████████████▌▌\n"
"▐─▀▀▀▐█▌▀▀███▀█─▌\n"
"▐▄───▄█───▄█▌▄█\n")

@kgbot.on(admin_cmd(pattern=r"crab"))
async def nandycrab(crab):
    await crab.edit(N)
@kgbot.on(admin_cmd(pattern=r"piano"))
async def nandypiano(piano):
    await piano.edit(M)
@kgbot.on(admin_cmd(pattern=r"man"))
async def nandyman(man):
    await man.edit(QQ)
@kgbot.on(admin_cmd(pattern=r"lion"))
async def nandylion(lion):
    await lion.edit(WW)
@kgbot.on(admin_cmd(pattern=r"elephant"))
async def nandyelephant(elephant):
    await elephant.edit(EE)
