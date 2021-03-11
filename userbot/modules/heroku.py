import os
import math
import heroku3
import asyncio
import urllib3
import requests
from userbot import HEROKU_APPNAME, HEROKU_APIKEY
from userbot.events import register as r
from userbot.cmdhelp import CmdHelp as c
from telethon import events
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(HEROKU_APIKEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = HEROKU_APPNAME
HEROKU_API_KEY = HEROKU_APIKEY


@r(pattern=r".(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)",outgoing=True)
async def variable(var):
    """
        Config Vars ayarlarının çoğunu yönetin, yeni değişken ayarlayın, mevcut değişkeni alın veya değişkeni silin...
    """
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        return await var.edit("`[HEROKU]:","\nLütfen kurulumunu yap` **HEROKU_APP_NAME**")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        fireqanq = await var.edit("`Bilgi alınıyor...`")
        await asyncio.sleep(1.0)
        
        variable = var.pattern_match.group(2).split()[0]
        if variable in heroku_var:
            return await fireqanq.edit("**ConfigVars**:",f"\n\n`{variable} = {heroku_var[variable]}`\n")
        return await fireqanq.edit("**ConfigVars**:",f"\n\n`Error:\n-> {variable} don't exists`")
    if exe == "set":
        fireqanq = await var.edit("`Ayar bilgileri...`")
        variable = var.pattern_match.group(2)
        if not variable:
            return await fireqanq.edit(">`.set var <ConfigVars-name> <value>`")
        value = var.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = var.pattern_match.group(2).split(' ', 1)[1]
            except IndexError:
                return await fireqanq.edit(">`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await fireqanq.edit(f"`{variable}`** başarıyla  **`{value}` **olarak değiştirildi**")
        else:
            await fireqanq.edit(f"`{variable}`**  değerle başarıyla eklendi`  ->  **{value}`")
        heroku_var[variable] = value
    elif exe == "del":
        fireqanq = await var.edit("`Değişkeni silmek için bilgi alma...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await fireqanq.edit("`Lütfen silmek istediğiniz Config Vars'ı belirtin`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await fireqanq.edit(f"`{variable}`  **Başarıyla silindi**")
            del heroku_var[variable]
        else:
            return await fireqanq.edit(f"`{variable}`**  mevcut değil**")


@r(pattern=".herokulogs$", outgoing=True)
async def _(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(" Lütfen Heroku API Anahtarınızın, Uygulama adınızın heroku'da doğru şekilde yapılandırıldığından emin olun")
    data = app.get_log()
    key = requests.post('https://nekobin.com/api/documents',
                        json={"content": data}).json().get('result').get('key')
    url = f'https://nekobin.com/{key}'
    reply_text = f'Son 100 satır heroku günlüğüs: [burada]({url})'
    await var.edit(dyno, reply_text)

a_=c("heroku")
a_.add_command(
    "set var <NEW VAR> <VALUE>", "Yeni Değişken Ekleyin Veya Mevcut Değer Değişkenini Güncelleyin")
a_.add_command("get var veya .get var <VAR>","Mevcut Değişkenlerinizi Alın!")
a_.add_command("del var <VAR>", "Mevcut Değişkeni Sil")
a_.add_command("herokulogs", "Size Heroku'daki Son 100 Satırlık Günlükleri Gönderir")
a_.add()
