import os
import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon import events
from userbot.events import register as r
from userbot import bot
from userbot.cmdhelp import CmdHelp as c



@r(outgoing=True, pattern=r"^.tts(?: |$)([\s\S]*)")
async def _(event):
    if event.fwd_from:
        return
    ttss = event.pattern_match.group(1)
    rep_msg = None
    if event.is_reply:
        rep_msg = await event.get_reply_message()
    if len(ttss) < 1:
        if event.is_reply:
            sarki = rep_msg.text
        else:
            await event.edit("`Sese çevirmem için komutun yanında bir mesaj yazmalısın.`")
            return

    await event.edit(f"__Metniniz sese çevriliyor...__")
    chat = "@MrTTSbot"
    async with bot.conversation(chat) as conv:
        try:     
            await conv.send_message(f"/tomp3 {ttss}")
        except YouBlockedUserError:
            await event.reply(f"`Mmmh sanırım` {chat} `engellemişsin. Engelini Açıyorum!`")
            await event.client(UnblockRequest(1678833172))

        ses = await conv.wait_event(events.NewMessage(incoming=True,from_users=1678833172))
        await event.client.send_read_acknowledge(conv.chat_id)
        indir = await ses.download_media()
        voice = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' -c:a libopus 'MrTTSbot.ogg'")
        await voice.communicate()
        if os.path.isfile("MrTTSbot.ogg"):
            await event.client.send_file(event.chat_id, file="MrTTSbot.ogg", voice_note=True, reply_to=rep_msg)
            await event.delete()
            os.remove("MrTTSbot.ogg")
        else:
            await event.edit("`Bir hata meydana geldi!`")

c_=c("tts").add_command(
    "tts", "<text/yanıt>", "Verdiğiniz Metni Ses e Dönüştürür!"
    ).add()