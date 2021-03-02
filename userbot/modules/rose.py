# ======================================================
"""                 @FireqanqUserBot                 """
# ======================================================

import os
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.cmdhelp import CmdHelp

chat = "@MissRose_bot"

@register(outgoing=True, pattern="^.rfstat ?(.*)")
async def fstat(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)
    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + kullanıcı + " " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + kullanıcı + " " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + text_)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()


@register(outgoing=True, pattern="^.rinfo ?(.*)")
async def info(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)
        
    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()


@register(outgoing=True, pattern="^.rfedinfo ?(.*)")
async def fedinfo(event):
    if event.fwd_from:
        return
    text_ = event.pattern_match.group(1)
    if text_ == "" and not event.reply_to_msg_id:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo " + text_)
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()


@register(outgoing=True, pattern="^.rmyfeds ?(.*)")
async def myfeds(event):
    if event.fwd_from:
        return
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await fedstat.click(0)
                reply = await conv.get_response()
                await event.client.send_message(event.chat_id, reply)
            else:
                await event.client.send_message(event.chat_id, myfed)
                await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("609517172"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await fedstat.click(0)
                reply = await conv.get_response()
                await event.client.send_message(event.chat_id, reply)
            else:
                await event.client.send_message(event.chat_id, myfed)
                await event.delete()
            
@register(outgoing=True, pattern="^.rfban ?(.*)")
async def fban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)
        
    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                
@register(outgoing=True, pattern="^.runfban ?(.*)")
async def unfban(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)
        
    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                
@register(outgoing=True, pattern="^.rfeddemote ?(.*)")
async def feddemote(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)
        
    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/feddemode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/feddemode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/unfban " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/feddemode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
                
@register(outgoing=True, pattern="^.rfpromode ?(.*)")
async def fpromode(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text_ = event.pattern_match.group(1)
        
    else:
        text_ = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        kullanıcı = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromode " + text_)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.client(UnblockRequest("609517172"))
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fpromode " + kullanıcı)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            
CmdHelp('rose').add_command(
    'rfstat', '<tag/id>', 'Sadece .rfstat Yazarsanız Kendiniz İçin Fban Listesini Verir. \n ID veya @KULLANICI ADI Verirseniz O Kişinin Fban Listesini Verir '
).add_command(
    'rinfo', '<tag/id>', 'Sadece .rinfo Yazarsanız kendiniz için Bilgi verir. \n ID veya @KULLANICI ADI Verirseniz O Kişi İçin Bilgi Veri.'
).add_command(
    'rfedinfo', '<fed id>', 'Sadece .rfedinfo yazarsanız Sizin Federasyonunuz İçin Bilgi Verir. \n FED İD Girerseniz O Federasyonun Bilgisini Verir'
).add_command(
    'rmyfeds', 'Hangi Federasyonlardan Yetkinizin Olduğunu Gösterir.'
).add_command(
    'rfban', '<tag/id>', 'Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fban atabilirsiniz. '
).add_command(
    'runfban', '<tag/id>', ' Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fbanını Açabilirsiniz. '
).add_command(
    'rfpromote', '<tag/id>', ' Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fban Yetkisi Verebilirsiniz. '
).add_command(
    'rfeddemote', '<tag/id>', ' Bunu Federasyon Sahipleri Kullana Bilir.\n Bulunduğunuz Gruptaki Kişiye Kendi Federasyonunuzdan Fban yetkisini Alabilirsiniz. \n NOT: BU KOMUTLAR HER YERDE ÇALIŞMAKTADIR ÖZEL MESAJLARDA VER HANGİ BİR GRUPTA KULLANA BİLİRSİNİZ @FireqanqUserBot '
    
).add()
