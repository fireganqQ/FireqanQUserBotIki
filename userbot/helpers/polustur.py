from telethon import events
dosya_name = 0
def edit_(q, m_split, sleep_t, name):
	global dosya_name
	dosya_name=1+dosya_name

	slep = sleep_t if sleep_t else 1.6

	f = open(f"{dosya_name}.py", "x")

	f.write(f"""
from userbot.events import register as r
from time import sleep
from telethon import events

@r(outgoing=True, pattern=".{name}")
async def _(q):
	for i in {m_split}:
		q.edit(i)
		sleep({slep})
		""")
	await q.client.send_file(q.chat_id, f, caption="Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")

def alt_(q, m_split, sleep_t, name):
	global dosya_name

	slep = sleep_t if sleep_t else 1.6
	dosya_name=1+dosya_name
	f = open(f"{dosya_name}.py", "x")

	f.write(f"""
from userbot.events import register as r
from time import sleep
from telethon import events

@r(outgoing=True, pattern=".{name}")
async def _(q):
	text = " "
	for i in {m_split}:
		text+=i
		q.edit(text)
		sleep({slep})
		""")
	await q.client.send_file(q.chat_id, f, caption="Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")