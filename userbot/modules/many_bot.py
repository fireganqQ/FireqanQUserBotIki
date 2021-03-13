import os
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from branch import branch

chat = "@manybot"

@register(outgoing=True, pattern="^.manybot ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    try:
        branch(event)
        return
    except:
        pass
    if event.pattern_match.group(1):
        text = event.pattern_match.group(1)
        
    else:
        await event.edit("`Bana Bir Bot Tokeni Vermelisin!!`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/addbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("74376339"))
            await conv.send_message("/addbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message("/skip")
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()

add_ = CmdHelp('manybot')
add_.add_command("manybot", "<bot_token>", "@manybot İle Botunuzu Oluşturun").add()
