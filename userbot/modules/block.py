#===============================================================================
"""             @fireganqQ tarafından @FireqanQUserBot a yapılmıştır         """
#===============================================================================
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import User
from userbot.events import register
from userbot import BOTLOG, BOTLOG_CHATID, WHITELIST
from userbot.cmdhelp import CmdHelp
import random
#===============================================================================


@register(outgoing=True, pattern=".block (.*)$")
async def _(block):
    sebep= block.pattern_match.group(1)
    if block.reply_to_msg_id:
        reply= await block.get_reply_message()
        r_user= await block.client.get_entity(reply.from_id)
        
        if r_user.id == WHITELIST:
            await block.edit("`Hayır dostum! @fireganqQ 'ı Engellemeyeceğim!!`")
            return
        id = r_user.id
        first_name = str(r_user.first_name)
        if r_user.last_name:
            last_name = str(r_user.last_name)

        else:
            last_name = ""

        username = "@" + r_user.username if r_user.username else f"[{first_name} {last_name}](tg://user?id={id})"
        mention = f"[{first_name} {last_name}](tg://user?id={id})"
        await block.client(BlockRequest(r_user.id))
        await block.edit(f"**#ENGELLENDI**\n`Kullancı: `{mention}\n`Sebebi: {sebep}`")
    else:
        if block.chat_id == WHITELIST:
            await block.edit(
                "`Hayır dostum! @fireganqQ'ı engellemeyeceğim!!`"
            )
            return

        await block.client(BlockRequest(block.chat_id))
        replied_user = await block.client.get_entity(block.chat_id)
        id = replied_user.id
        first_name = str(replied_user.first_name)
        if replied_user.last_name:
            last_name = str(replied_user.last_name)
        else:
            last_name = ''

        username = '@' + replied_user.username if replied_user.username else f'[{first_name} {last_name}](tg://user?id={id})'
        mention = f'[{first_name} {last_name}](tg://user?id={id})'

        await block.edit(f"**#ENGELLENDI**\n`Kullancı: `{mention}\n`Sebebi: {sebep}`")
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
        dissprove(id)
    except:
        pass

    if BOTLOG:
        await block.client.send_message(
            BOTLOG_CHATID,
            f"**#ENGELLENDI**\n`Kullancı: `{mention}\n`Sebebi: {sebep}`")

#===============================================================================

SEBEP=["Sanane Canım İstedi!!", " ", "Dostum Bana Yazmayı Kes!!", "Seni Sevmiyorum O yüzden Engeli Hakettin!!"]

@register(outgoing=True, pattern=".block$")
async def _(block):
    if block.reply_to_msg_id:
        reply= await block.get_reply_message()
        r_user= await block.client.get_entity(reply.from_id)
        id = r_user.id
        if r_user.id == WHITELIST:
            await block.edit("`Hayır dostum! @fireganqQ 'ı Engellemeyeceğim!!`")
            return

        first_name = str(r_user.first_name)
        if r_user.last_name:
            last_name = str(r_user.last_name)

        else:
            last_name = ""

        username = "@" + r_user.username if r_user.username else f"[{first_name} {last_name}](tg://user?id={id})"
        mention = f"[{first_name} {last_name}](tg://user?id={id})"
        await block.client(BlockRequest(r_user.id))
        await block.edit(f"**#ENGELLENDI**\n`Kullancı: `{mention}\n`Sebebi: {random.choice(SEBEP)}`")
    else:
        if block.chat_id == WHITELIST:
            await block.edit(
                "`Hayır dostum! @fireganqQ'ı engellemeyeceğim!!`"
            )
            return

        await block.client(BlockRequest(block.chat_id))
        replied_user = await block.client.get_entity(block.chat_id)
        id = replied_user.id
        first_name = str(replied_user.first_name)
        if replied_user.last_name:
            last_name = str(replied_user.last_name)
        else:
            last_name = ''

        username = '@' + replied_user.username if replied_user.username else f'[{first_name} {last_name}](tg://user?id={id})'
        mention = f'[{first_name} {last_name}](tg://user?id={id})'

        await block.edit(f"**#ENGELLENDI**\n`Kullancı: `{mention}\n`Sebebi: {random.choice(SEBEP)}`")
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
        dissprove(id)
    except:
        pass

    if BOTLOG:
        await block.client.send_message(
            BOTLOG_CHATID,
            f"**#ENGELLENDI**\n`Kullancı: `{mention}\n`Sebebi: {random.choice(SEBEP)}`")
CmdHelp("block").add_command(
    "block",
    "<İsteğe bağlı sebep>",
    "Kullanıcıyı Engeller!"
).add()
