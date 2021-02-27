
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError

def help_(event, audio):
	try:
		await event.client.forward_messages("162726413", audio)
		await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
	except YouBlockedUserError:
		await event.client(UnblockRequest("162726413"))
		await event.client.forward_messages("162726413", audio)
		await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")