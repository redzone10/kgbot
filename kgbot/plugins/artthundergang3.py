"""Plugin made by kgproject1010 for kgbot 
and if you will copy it without credits then you are the biggest gay of this universe"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from kgbot.utils import admin_cmd

P = ("───▄█▌─▄─▄─▐█▄\n"
"───██▌▀▀▄▀▀▐██\n"
"───██▌─▄▄▄─▐██\n"
"───▀██▌▐█▌▐██▀\n"
"▄██████─▀─██████▄\n")
A = ("░░░░░░░▄█▄▄▄█▄\n"
"▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄\n"
"█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█\n"
"░▐▌░░░░▀▀███▀▀░░░░▐▌\n"
"████░▄█████████▄░████\n")
S = ("▄▄▀█▄───▄───────▄\n"
"▀▀▀██──███─────███\n"
"░▄██▀░█████░░░█████░░\n"
"███▀▄███░███░███░███░▄\n"
"▀█████▀░░░▀███▀░░░▀██▀\n")
D = ("╔══╗░░░░╔╦╗░░╔═════╗\n"
"║╚═╬════╬╣╠═╗║░▀░▀░║\n"
"╠═╗║╔╗╔╗║║║╩╣║╚═══╝║\n"
"╚══╩╝╚╝╚╩╩╩═╝╚═════╝\n")
F = ("───────███\n"
"───────███\n"
"▄█████▄█▀▀\n"
"─▀█████\n"
"──▄████▄\n")

@kgbot.on(admin_cmd(pattern=r"devil"))
async def nandydevil(devil):
    await devil.edit(P)
@kgbot.on(admin_cmd(pattern=r"robot"))
async def nandyrobot(robot):
    await robot.edit(A)
@kgbot.on(admin_cmd(pattern=r"boa"))
async def nandyboa(boa):
    await boa.edit(S)
@kgbot.on(admin_cmd(pattern=r"smile"))
async def nandysmile(smile):
    await smile.edit(D)
@kgbot.on(admin_cmd(pattern=r"toilet"))
async def nandytoilet(toilet):
    await toilet.edit(F)
