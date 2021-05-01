from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from time import sleep

durDur = False
allSorgu = None
allLimit = 100

@r(outgoing=True, pattern="^.all(?: |$)(.*)")
async def _(q):
	global durDur
	global allSorgu
	if q.fwd_from:
		return
	try:
		from userbot import BOT_NAME as bn
		if bn != "fg":
			await q.edit("`Hey! Dostum` @FireqanqUserBot `Kullanmıyorsun!!!`")
			return
	except:
		await q.edit("`Hey! Dostum` @FireqanqUserBot `Kullanmıyorsun!!!`")
		return

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	allSorgu = True
	await q.delete()
	async for i in bot.iter_participants(chat):
		if durDur:
			durDur=False
			allSorgu = None
			break
		if a_ == allLimit:
			durDur=False
			allSorgu = None
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		if allLimit <= 100:
			sleep(1)
		if allLimit > 100:
			sleep(2)


@r(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def _(q):
	global durDur
	global allSorgu

	if q.fwd_from:
		return
	try:
		from userbot import BOT_NAME as bn
		if bn != "fg":
			await q.edit("`Hey! Dostum` @FireqanqUserBot `Kullanmıyorsun!!!`")
			return
	except:
		await q.edit("`Hey! Dostum` @FireqanqUserBot `Kullanmıyorsun!!!`")
		return

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	allSorgu = True
	await q.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if durDur:
			durDur=False
			allSorgu = None
			break
		if a_ == allLimit:
			durDur=False
			allSorgu = None
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		if allLimit <= 100:
			sleep(1)
		if allLimit > 100:
			sleep(2)

@r(outgoing=True, pattern="^.allstop$")
async def _(q):
	global durDur
	if allSorgu == None:
		await q.edit("`Aktif Bir All Yok!!`")
		return

	durDur = True
	await q.edit("`All Durduruldu!`")

@r(outgoing=True, pattern=".all[lL]imit(?: |$)(.*)$")
async def _(q):
	global allLimit
	limit = q.pattern_match(1)
	if len(limit) < 1:
		return await q.edit("`Lütfen Bana Bir İntager Değer Veriniz!!`")
	try:
		limit=int(limit)
	except:
		await q.edit("`Lütfen Bana Bir İntager Değer Vermediniz!!`")
		return

	allLimit=limit
	await q.edit("`All Değeriniz {} Olarak Değiştirildi!`".format(str(limit)))

c("all").add_command(
	"all", "<sebep(isteğe bağlı)>", "İstediğiniz grupta all max 100 kişi yi etiketlersiniz!"
	).add_command(
	"alladmin", "<sebep(isteğe bağlı)>", "İstediğiniz grupta tüm adminleri etiketlersiniz!"
	).add_command(
	"allstop", None, "Aktif All Varsa Durdurur!"
	).add_command(
	"alllimit", "<all_limiti/boş bıraklılırsa eski halie döner>", "All Limitinizi Ayarlarsınız"
	).add()
