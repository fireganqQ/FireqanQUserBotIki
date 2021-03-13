from userbot.helpers.polustur import edit_, alt_, dosya_name
from branch import branch
from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events

@r(outgoing=True, pattern="^.polu[sş]tur (.*) (.*) (edit|alt)$")
async def _(q):
	try:
		branch(q)
		return
	except:
		if q.is_reply:
			mesaj = await q.get_reply_message()
			name = q.pattern_match.group(1)
			sleep_t = q.pattern_match.group(2)
			sec = q.pattern_match.group(3)

			if name == "":
				await q.edit("**Hey, Dostum Pluginin İçin Bir Komut Vermelisim!!**")
				return

			else:
				if sleep_t == "":
					await q.edit("**Hey, Dostum Pluginin Hızını Belirtmelisin!!**")
					return

				else:
					if sec == "":
						await q.edit("**Hey, Dostum Pluginin Nasıl Olmasını İstediğini Belirtmelisin!!**")
						return

					else:
						if sec == "edit":
							m_split = mesaj#.split("\n")
							edit_(q, m_split, sleep_t, name)
							await q.client.send_file(q.chat_id, f"./{dosya_name}.py", caption="Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")

						if sec == "alt":
							m_split = mesaj#.split("/e")
							alt_(q, m_split, sleep_t, name)
							await q.client.send_file(q.chat_id, f"./{dosya_name}.py", caption="Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")

						else:
							await q.edit("**Hey, Dostum Gecersiz Bir Metin Belirttin!!**")
							return



		else:
			await q.edit("**Hey, Dostum Bir Mesajı Yanıtlamalısın!!**")
