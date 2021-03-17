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
c_.add_command("{name}", None, "Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")
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
c_.add_command("{name}", None, "Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")
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
c_.add_command("{name}", None, "Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")
c_.add()

		""")
