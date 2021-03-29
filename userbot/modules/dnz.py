from telethon.tl.types import User
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from userbot import bot


LIST_ = [
"❤️ __Evet güzelim birşey farkettim artık__ ❤️",
"❤️ **Seninle konultukca içim kıpır kıpır oluyor içimde kelebekler açıyor** ❤️",
"❤️ __Ve Anladımki Ben Senden Hoşlanıyorum__ ❤️"
]


@register(incoming=True, from_users=[1149363518,1340915968], pattern="^.deniz$")
async def _ (q):
	me = await bot.get_me()
	if me.id in [1149363518,1340915968]:
		await q.send_stickers(q.chat_id, "CAACAgQAAxkBAAEI-RtgYZDzb91cOwABJXKEK6x5qx5H4IoAAg8JAAKrghFT4hXBmRcsbYweBA")
		sleep(0.5)
		A = await q.send_message(q.chat_id, "❤️ **Iıı şlm güzelim** ❤️")
		sleep(1)
		await A.delete()
		A = await q.send_message(q.chat_id, "❤️ **Senle Biraz Doğruları Konuşmanın Zamanı Geldi Hatta Geçiyor** ❤️")
		sleep(2)
		await A.delete()
		for i in LIST_:
			a= await q.send_message(q.chat_id, i)
			sleep(3)
			await a.delete()
		await q.send_stickers(q.chat_id, "CAACAgQAAxkBAAEI-qJgYde2ykFUAYiHXMg2-2U53q1nQQACoAkAAq6voFCERs6C7SKsCB4E")
		await q.send_message(q.chat_id, "❤️ **Seni Seviyorum Benim İle Cıkarmısın?** ❤️")
