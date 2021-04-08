def e_(dosya_name, name, slep, liste):
	f = open(f"./fguserbot{dosya_name}.py", "x")
	f.write(f"""from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from time import sleep as s
from telethon import events

a={liste}

@r(outgoing=True, pattern="^.{name}$")
async def _(q):
	for i in a:
		await q.edit(' '+str(i))
		s({slep})

c_ = c("fguserbot{dosya_name}")
c_.add_command("{name}", None, "Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
c_.add()
								""")
	return f.close()

def a_(dosya_name, name, liste, slep):
	f = open(f"./fguserbot{dosya_name}.py", "x")
	f.write(f"""from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from time import sleep as s
from telethon import events

a={liste}

@r(outgoing=True, pattern="^.{name}$")
async def _(q):
	text= " "
	for i in a:
		text+=i+"\\n"
		await q.edit(text)
		s({slep})

c_ = c("fguserbot{dosya_name}")
c_.add_command("{name}", None, "Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
c_.add()
								""")
	return f.close()

def r_(dosya_name, name, liste):
	f = open(f"./fguserbot{dosya_name}.py", "x")
	f.write(f"""from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events
from random import choice

a={liste}

@r(outgoing=True, pattern="^.{name}$")
async def _(q):
	random_ = choice(a)
	await q.client.send_file(q.chat_id, random_)
	await q.delete()

c_ = c("fguserbot{dosya_name}")
c_.add_command("{name}", None, "Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
c_.add()

		""")

def m_(dosya_name, name, liste):
	f = open(f"./fguserbot{dosya_name}.py", "x")
	f.write(f"""from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events
import random
import os

SARKILAR = [{liste}]
SARKICI = str(SARKILAR[0])
SARKILAR.pop(0)

@r(outgoing=True, pattern="^.{name}$")
async def _(q):
    sarki = random.choice(SARKILAR)
    await q.edit(f"`{sarki} Sakısını Arıyorum!`")

    try:
        try:
            sonuclar = await q.client.inline_query(f'deezermusicbot {SARKICI}" "{sarki}')
        except:
            await q.edit("`Üzgünüm, bottan yanıt alamadım!`")
            return

        true_but_false = True
        while true_but_false == True:
            rast = random.choice(sonuclar)
            if rast.description == SARKICI:
                await q.edit("`Şarkı indiriliyor! Lütfen bekleyiniz...`")
                indir = await rast.download_media()
                await q.edit("`İndirme tamamlandı! Dosyayı Gönderiyorum...`")
                await q.client.send_file(q.chat_id, indir, caption=f"@FireqanqUserBot Senin İçin `{rast.description} - {rast.title}` Seçti\n\n🎵Iyi Dinlemeler🎧")
                await event.delete()
                os.remove(indir)
                true_but_false=False

    except:
        q.edit("`Şarkıyı Bulamadım`\n**Yanlış Sarkıcı İsmi Veya Yanlış Şarkı İsmi Girdiniz!!**")
        return

c_ = c("fguserbot{dosya_name}")
c_.add_command("{name}", None, "Bu Plugin @FireqanqUserBot Tarafından Yapılmıştır..")
c_.add()


		""")
