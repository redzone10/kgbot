"""Plugin made by kgproject1010 for kgbot
and if you will copy it without credits then you are the biggest gay of this universe"""
from kgbot.utils import admin_cmd

G = (
    "▄█▀─▄▄▄▄▄▄▄─▀█▄\n"
    "▀█████████████▀\n"
    "────█▄███▄█\n"
    "─────█████\n"
    "─────█▀█▀█\n"
)
H = (
    "───▄▄─▄████▄▐▄▄▄▌\n"
    "──▐──████▀███▄█▄▌\n"
    "▐─▌──█▀▌──▐▀▌▀█▀\n"
    "─▀───▌─▌──▐─▌\n"
    "─────█─█──▐▌█\n"
)
J = (
    "──▄──▄────▄▀\n"
    "───▀▄─█─▄▀▄▄▄\n"
    "▄██▄████▄██▄▀█▄\n"
    "─▀▀─█▀█▀▄▀███▀\n"
    "──▄▄▀─█──▀▄▄\n"
)
K = (
    "░╔╔╩╩╝\n"
    "▄██▄\n"
    "░░██████▄░░░░░░▄▄▄▄▄▄█\n"
    "░░█▀█▀█▀█░░▄░▄████████\n"
    "░▄▌▄▌▄▌▄▌░▀▄▄▄▄█▄▄▄▄█▄\n"
)
L = (
    "█───▄▀▀▀▀▄─▐█▌▐█▌▐██\n"
    "█──▐▄▄────▌─█▌▐█─▐▌─\n"
    "█──▐█▀█─▀─▌─█▌▐█─▐██\n"
    "█──▐████▄▄▌─▐▌▐▌─▐▌─\n"
    "███─▀████▀───██──▐██\n"
)


@kgbot.on(admin_cmd(pattern=r"bull"))
async def nandybull(bull):
    await bull.edit(G)


@kgbot.on(admin_cmd(pattern=r"fox"))
async def nandyfox(fox):
    await fox.edit(H)


@kgbot.on(admin_cmd(pattern=r"spider"))
async def nandyspider(spider):
    await spider.edit(J)


@kgbot.on(admin_cmd(pattern=r"winter"))
async def nandywinter(winter):
    await winter.edit(K)


@kgbot.on(admin_cmd(pattern=r"love"))
async def nandylove(love):
    await love.edit(L)
