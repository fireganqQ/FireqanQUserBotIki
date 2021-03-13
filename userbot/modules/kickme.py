from userbot.language import get_value
LANG = get_value("chat")

from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot.main import PLUGIN_MESAJLAR
from branch import branch


@register(outgoing=True, pattern="^.k[iı]ckme$")
async def kickme(leave):
    try:
        branch(leave)
        return
    except:
        pass
    """ .kickme komutu gruptan çıkmaya yarar """
    chat = await leave.get_chat()
    await leave.edit(f"{PLUGIN_MESAJLAR['kickme']}".format(
        id=chat.id,
        title=chat.title,
        member_count="Bilinmiyor" if chat.participants_count == None else (chat.participants_count - 1)
    ))
    await leave.client.kick_participant(leave.chat_id, 'me')

# ===================================================================================

@register(outgoing=True, pattern="^.k[iı]ckme (.*)$")
async def kickme(leave):
    try:
        branch(leave)
        return
    except:
        pass
    """ .kickme komutu gruptan çıkmaya yarar """
    chat = await leave.get_chat()
    sebep= leave.pattern_match.group(1)
    await leave.edit(f"**🤠Güle Güle Ben Gidiyorum!🤠\nSebep:** `{sebep}`")
    await leave.client.kick_participant(leave.chat_id, 'me')


CmdHelp("kickme").add_command(
    "kickme",
    "<İsteğe bağlı sebep>",
    "Sizi Grupdan Cıkarır!"
).add()
