import asyncio
import telethon
from userbot.events import register
from telethon import events
from userbot.cmdhelp import CmdHelp
from userbot import bot
from branch import branch


msg_ = "Verdiğiniz Mesaj FireqanqUserBot Tarafından **Kayıtlı Mesajlara** Gönderilmiştir!!"
yanıt_msg = "Yanıtınız FireqanqUserBot Tarafından **Kayıtlı Mesajlara** Gönderilmiştir!!"


@register(outgoing=True, pattern="^.kyolla$")
async def _(qwe):
  try:
    branch(qwe)
    return
  except:
    pass
  if qwe.is_reply:
    mesaj = await qwe.get_reply_message()
  else:
    await qwe.edit("`Bir mesaja yanıt ver veya bana bir mesaj ver!!`")
    return
  await qwe.client.forward_messages("me", mesaj)
  await qwe.edit(yanıt_msg)



@register(outgoing=True, pattern="^.kyolla (.*)$")
async def _(qwe):
  try:
    branch(qwe)
    return
  except:
    pass
  mesaj = qwe.pattern_match.group(1)
  await bot.send_message("me", mesaj)
  await qwe.edit(msg_)
  






add_=CmdHelp('kyolla')
add_.add_command('kyolla', '<Bir mesaja yanıt ver veya bana bir mesaj ver>', 'Verdiğiniz/Yanıtladığınız Mesajı Kayıtlı Mesajlara Gönderir')
add_.add()
