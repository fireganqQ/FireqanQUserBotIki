import os
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError

def helpolustur(event, text, username):
    async with event.client.conversation("@BotFather") as conv:
        try:
            from userbot.modules.sql_helper.h1 import help_
        except:
            await event.edit("Sql Mod Dışında Calışıyor!!")
            return
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            help_(event, audio)
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            help_(event, audio)