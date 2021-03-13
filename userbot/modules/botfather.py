# ======================================================
"""                 @FireqanqUserBot                 """
# ======================================================

import os
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from branch import branch

chat = "@BotFather"

@register(outgoing=True, pattern="^.newbot ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    try:
        branch(event)
        return
    except:
        pass
    if event.pattern_match.group(1):
        text, username= event.pattern_match.group(1).split()
        
    else:
        await event.edit("`Bana Bot İçin Bir Username Vermelisin!!`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()



add_ = CmdHelp('botfather')
add_.add_command("newbot", "<bot_name><bot_username>", "Yeni Bot Oluşturun").add()
