#===============================================================================
"""             @fireganqQ tarafından @FireqanQUserBot a yapılmıştır         """
#===============================================================================
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import User
from userbot.events import register
from userbot import BOTLOG, BOTLOG_CHATID, WHITELIST
from userbot.cmdhelp import CmdHelp
from userbot.main import PLUGIN_MESAJLAR
#===============================================================================

@register(outgoing=True, pattern="^.unblock (.*)$")
async def unblockpm(unblock):
    """ .unblock komutu insanların size yeniden PM atabilmelerini sağlar. """
    sebep= unblock.pattern_match.group(1)
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client.get_entity(reply.from_id)
        name0 = str(replied_user.first_name)
        mention= f"[{name0}](tg://user?id={replied_user.id})"
        await unblock.client(UnblockRequest(replied_user.id))
        await unblock.edit(f"**#UNBLOCK**\n`Kullancı: `{mention}\n`Sebebi: {sebep}`")

    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"**#UNBLOCK**\n`Kullancı: `{mention}\n`Sebebi: {sebep}`")


@register(outgoing=True, pattern="^.unblock$")
@register(incoming=True, from_users=WHITELIST, pattern="^.aunblock$")
async def unblockpm(unblock):
    """ .unblock komutu insanların size yeniden PM atabilmelerini sağlar. """
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client.get_entity(reply.from_id)
        name0 = str(replied_user.first_name)
        await unblock.client(UnblockRequest(replied_user.id))
        await unblock.edit(PLUGIN_MESAJLAR['unblock'].format(
            name0=name0,
            replied_userid=replied_user.id
            ))

    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={replied_user.id})"
            " kişisinin engeli kaldırıldı.",
        )
CmdHelp('unblock').add_command(
    'unblock', '<kullanıcı adı/yanıtlama>', 'Kullanıcının engellemesini kaldırır.'
).add()
