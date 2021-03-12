import requests
import time
from PIL import Image
from telethon import version
from userbot import StartTime
from platform import python_version
from userbot import ALIVE_NAME, fgdef, FİREQANQ_VERSION, ALIVE_PIC, bot, ALIVE_ID_USER, CMD_HELP
from userbot.events import register
from telethon import events
from userbot.main import PLUGIN_MESAJLAR

ALİVE_ = True
ALİVE_N_ = None
ALİVE_I_ = None
ALİVE_P_ = None

def degiskenler():
	if ALİVE_:
		if ALİVE_N_:
			DEFAULTUSER = ALİVE_N_
			if ALİVE_I_:
				id_ = f"[{DEFAULTUSER}](tg://user?id={int(ALİVE_I_)})"
				if ALİVE_P_:
					ALIVE_PIC = ALİVE_P_
				else:
					ALIVE_PIC= ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c0d18f7499d737c43bd9d.mp4"
			else:
				id_ = f"[{DEFAULTUSER}](tg://user?id={int(ALIVE_ID_USER)})" if ALIVE_ID_USER else DEFAULTUSER
		else:
			DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "FireqanqUserBot"
			if ALİVE_I_:
				id_ = f"[{DEFAULTUSER}](tg://user?id={int(ALİVE_I_)})"
				if ALİVE_P_:
					ALIVE_PIC = ALİVE_P_
				else:
					ALIVE_PIC= ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c0d18f7499d737c43bd9d.mp4"
			else:
				id_ = f"[{DEFAULTUSER}](tg://user?id={int(ALIVE_ID_USER)})" if ALIVE_ID_USER else DEFAULTUSER


@register(outgoing=True, pattern="^.alive")
async def amireallyalive(a):
	if a.fwd_from:
		return
	degiskenler()

	if ALİVE_:
		reply_to_id = a.message
		uptime = await fgdef.get_readable_time((time.time() - StartTime))
		_, check_sgnirts = check_data_base_heal_th()
		if a.reply_to_msg_id:
			reply_to_id = await a.get_reply_message()
		fg_caption = f"__**✮ FireqanqUserBot ÇALIŞIYOR ✮**__\n\n"
		fg_caption += f"**✧ Veri Tabanı :** `{check_sgnirts}`\n"
		fg_caption += f"**✧ Telethon Sürümü :** `{version.__version__}\n`"
		fg_caption += f"**✧ FireqanqUserBot Sürümü :** `{FİREQANQ_VERSION}`\n"
		fg_caption += f"**✧ Python Sürümü :** `{python_version()}\n`"
		fg_caption += f"**✧ Çalışma Süresi :** `{uptime}\n`"
		fg_caption += f"**✧ Benim Ustam :** {id_}\n"
		await bot.send_file(a.chat_id, ALIVE_PIC, caption=fg_caption, reply_to=reply_to_id)
		await a.delete()
	else:
		me = await a.client.get_me()
		await a.edit(PLUGIN_MESAJLAR['alive'].format(
            telethon=version.__version__,
            python=python_version(),
            fireqanq=FİREQANQ_VERSION,
            plugin=len(CMD_HELP),
            id=me.id,
            username='@' + me.username if me.username else f'[{me.first_name}](tg://user?id={me.id})',
            first_name=me.first_name,
            last_name=me.last_name if me.last_name else '',
            mention=f'[{me.first_name}](tg://user?id={me.id})'
        ))

def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "Veritabanı ayarlanmadı"
    from userbot.modules.sql_helper import SESSION
    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Normal Çalışıyor"
        is_database_working = True
    return is_database_working, output



@register(outgoing=True, pattern="^.([aA][Dd][eE][GgĞğ][Iıİi][SsŞş][Tt][Iıİi][rR]|[dD][eE][Ll]) (.*)")
async def _(q):
	global ALİVE_
	global ALİVE_N_
	global ALİVE_I_
	global ALİVE_P_

	a_=["alive","name","pic","id"]

	text = q.pattern_match.group().split()
	text.pop(0)

	try:
		text, text_2=text
		if text == "" and text == " ":
			await q.edit("`Gecersiz Değer Girdiniz Değiştire Bileceğiniz Değerler =>` `alive``/``name``/``pic``/``id`")
			return		
	except:
		await q.edit("`Gecersiz Değer Girdiniz Değiştire Bileceğiniz Değerler =>` `alive``/``name``/``pic``/``id`")
		return

	if text.lower() == "alive":
		if text_2.lower() != "true" and text_2.lower() != "false" or text_2.lower() == "":
			await q.edit("`Sadece True Veya False Giriniz...`")
			return
		else:
			if text_2.lower() == "true":
				ALİVE_ = True
				await q.edit("`Alive Değeriniz True Olarak Değiştirilmiştir...`")
				return

			if text_2.lower() == "false":
				ALİVE_ = False
				await q.edit("`Alive Değeriniz Fasle Olarak Değiştirilmiştir...`")
			return
	if text.lower() == "name":
		if text_2.lower() != "":
			ALİVE_N_=text_2
			await q.edit("`Name Değeriniz {} Olarak Değiştirilmiştir...`".format(text_2))
			return
		else:
			await q.edit("`Name Değişkenini Değiştirmem İçin Bana Bir İsim Vermelisim!!`")
			return

	if text.lower() == "pic":
		if text_2.lower() != "":
			ALİVE_P_=text_2
			await q.edit("`Alive Pic Linkiniz {} Olarak Değiştirilmiştir...`".format(text_2))
			return
		else:
			await q.edit("`Pic Değişkenini Değiştirmem İçin Bana Bir Link Vermelisim!!`")
			return

	if text.lower() == "id":
		if text_2.lower() != "":
			ALİVE_I_=text_2
			await q.edit("`İd Değişkeniniz {} Olarak Değiştirilmiştir...`".format(text_2))
			return
		else:
			await q.edit("`İd Değişkenini Değiştirmem İçin Bana Bir İd Vermelisim!!`")
