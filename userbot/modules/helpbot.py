import os
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot
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
            await event.client.forward_messages(entity=event.chat_id, messages=audio)
            await event.edit("`Botunuz Başarı İle Oluşturuldu!`")
            await bot.send_message(event.chat_id, "`Botfatherdan İleti Olan Mesajı @GroupHelpBot'a İleterek Kurulumu Tamamlaya Bilirsin!`")

        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(entity=event.chat_id, messages=audio)
            await event.edit("`Botunuz Başarı İle Oluşturuldu!`")
            await bot.send_message(event.chat_id, "`Botfatherdan İleti Olan Mesajı` @GroupHelpBot'a `İleterek Kurulumu Tamamlaya Bilirsin!`")

add_ = CmdHelp('helpbot')
add_.add_command("helpbot", "<bot_name> <bot_username>", "FireqanqUserBot İle Group Help Botu Clonlayın").add()
