import time
from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events
from branch import branch


@r(outgoing=True, pattern="^.sreply (.*)$")
async def _(q):
    try:
        branch(q)
        return
    except:
        if q.get_reply_message():
            sure_ = int(q.pattern_match.group(1))
            reply_ = await q.get_reply_message()
            text_ = reply_.text

            smsg = await q.client.send_message(q.chat_id, text_)
            await q.edit("`Mesaj {sure} Saniye İçinde Kendini Yok Edecek`".format(sure=sure_))

            time.sleep(sure_)
            await smsg.delete()

@r(outgoing=True, pattern="^.smsg (.*) ?(\w*)$")
async def _(q):
    try:
        branch(q)
        return
    except:
        text_ = q.pattern_match.group().split()
        sure_ = text_[1]
        msg_ = " "
        text_.remove(text_[0])
        text_.remove(text_[0])
        for i in text_:
            msg_+=i+" "
        smsg = await q.client.send_message(q.chat_id, msg_)
        await q.edit("`Mesaj {sure} Saniye İçinde Kendini Yok Edecek`".format(sure=sure_))
        time.sleep(int(sure_))
        await smsg.delete()

c('sureli').add_command(
    "sreply", "<mesajı_yanıtla + zaman>", "Yanıtladığınız Mesajı Belirttiğiz Saniye Sonra Kendini Yok Eder örnek: `.sreply 12`"
    ).add_command(
    "smsg", "<zaman> <text>", "Verdiğiniz Metin Belirttiğiniz Saniye Sonra Kendini Yok Eder. Örnek: `.smsg 12 Hey Dostum @FireqanqUserBot Cok Güzel Sende Kullansana!`"
    ).add()
