#import nekos
import requests
import time
from PIL import Image
from telethon import version
from userbot import StartTime
from platform import python_version
from userbot import ALIVE_NAME, fgdef, FİREQANQ_VERSION, ALIVE_PIC, bot, ID_USER
from userbot.events import register
from telethon import events

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "FireqanqUserBot"

id_ = ID_USER if ID_USER else "1340915968"

@register(outgoing=True, pattern="^.alive")
async def amireallyalive(a):
    if a.fwd_from:
        return
    reply_to_id = a.message
    uptime = await fgdef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if a.reply_to_msg_id:
        reply_to_id = await a.get_reply_message()
    if ALIVE_PIC:
        fg_caption = f"__**✮ FireqanqUserBot ÇALIŞIYOR ✮**__\n\n"
        fg_caption += f"**✧ Veri Tabanı :** `{check_sgnirts}`\n"
        fg_caption += f"**✧ Telethon Sürümü :** `{version.__version__}\n`"
        fg_caption += f"**✧ FireqanqUserBot Sürümü :** `{FİREQANQ_VERSION}`\n"
        fg_caption += f"**✧ Python Sürümü :** `{python_version()}\n`"
        fg_caption += f"**✧ Çalışma Süresi :** `{uptime}\n`"
        fg_caption += f"**✧ Benim Ustam :** [{DEFAULTUSER}](tg://user?id={int(id_)})\n"
        await bot.send_file(a.chat_id, ALIVE_PIC, caption=fg_caption, reply_to=reply_to_id)
        await a.delete()
    else:
        await a.edit(a, f"__**✮ FireqanqUserBot ÇALIŞIYOR ✮**__\n\n"
                            f"**✧ Veri Tabanı :** `{check_sgnirts}`\n"
                            f"**✧ Telethon Sürümü :** `{version.__version__}\n`"
                            f"**✧ FireqanqUserBot Sürümü :** `{FİREQANQ_VERSION}`\n"
                            f"**✧ Python Sürümü :** `{python_version()}\n`"
                            f"**✧ Çalışma Süresi :** `{uptime}\n`"
                            f"**✧ Benim Ustam :** [{DEFAULTUSER}](tg://user?id={id_})\n"
                            )


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
