from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events

dosya_name=0
@r(outgoing=True, pattern="^.polu[sş]tur (.*) (.*) (edit|alt)$")
async def _(q):
	global dosya_name
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
						liste=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							liste.append(i)
						dosya_name=dosya_name+1

						slep = sleep_t if sleep_t else 1.6

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
						f.close()
						#file = await q.client.upload_file(f'./fg{dosya_name}.py')
						await q.client.send_file(q.chat_id, f"./fguserbot{dosya_name}.py", force_document=True, caption="Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")
						await q.delete()
						return
					if sec == "alt":
						liste=[]
						m_split = mesaj.text.split("\n")
						for i in m_split:
							liste.append(i)
						dosya_name=dosya_name+1

						slep = sleep_t if sleep_t else 1.6

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
						f.close()
						#file = await q.client.upload_file(f'./fg{dosya_name}.py')
						await q.client.send_file(q.chat_id, f"./fguserbot{dosya_name}.py", force_document=True, caption="Bu Plugin @FireqanqUserBot Taradından Yapılmıştır..")
						await q.delete()
						return

					else:
						await q.edit("**Hey, Dostum Gecersiz Bir Metin Belirttin!!**")
						return



	else:
		await q.edit("**Hey, Dostum Bir Mesajı Yanıtlamalısın!!**")
		return
