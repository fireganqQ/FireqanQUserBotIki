import os
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.helpbot ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username= event.pattern_match.group(1).split()
        
    else:
        await event.edit("`Bana Botuna Vermemi İstediğin İsim İle username Vermelisin!!`")
        return

    async with event.client.conversation("@BotFather") as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            try:
                await event.client.forward_messages(str(162726413), audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
            except YouBlockedUserError:
                await event.client(UnblockRequest("162726413"))
                await event.client.forward_messages(str(162726413), audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            try:
                await event.client.forward_messages(str(162726413), audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
            except YouBlockedUserError:
                await event.client(UnblockRequest("162726413"))
                await event.client.forward_messages(str(162726413), audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")

add_ = CmdHelp('helpbot')
add_.add_command("helpbot", "<bot_name> <bot_username>", "Tek Komut İle Group Help Botu Clonlayın").add()
