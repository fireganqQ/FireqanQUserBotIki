import asyncio
import os
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from branch import branch


@register(outgoing=True, pattern="^.[Gg][Ii][Zz][Ll][Ii] ?(.*)")
async def _(e):
    if e.fwd_from:
        return
    try:
        branch(e)
        return
    except:
        pass
    wwwspr = e.pattern_match.group(1)

    botusername = "@whisperbot"
    if e.reply_to_msg_id:
        reply_to_id = await e.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr) 
    await tap[0].click(e.chat_id, 0)
    await e.delete()




add_=CmdHelp('gizli')
add_.add_command(
    "gizli", "Gruplarda Arkadaşlarınıza Gizli Mesajlar Göndere Bilirsiniz", "Örnek .gizli Sende @FireqanqUserBot Kursana @fireganqQ"
    )
add_.add_info("UNUTMA!! SON EYLEMLERDEN YÖNETİCİLER NE YAZDIĞINI GÖRE BİLİRLER")
add_.add()
