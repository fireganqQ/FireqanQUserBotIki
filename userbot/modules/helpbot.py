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
    
    try:
        from userbot.modules.sql_helper.he3per import helpolustur
    except:
        await event.edit("Sql Mod Dışında Calışıyor!!")
        return

    helpolustur(event, text, username)

add_ = CmdHelp('helpbot')
add_.add_command("helpbot", "<bot_name> <bot_username>", "Tek Komut İle Group Help Botu Clonlayın").add()