from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.[Oo][Ll][Uu][ŞşSs][Tt][Uu][Rr] (1|2|3)(?: |$)(.*)")
async def _(grup):
    veri = grup.pattern_match.group(1)
    chanl_name = grup.pattern_match.group(2)

    if veri == "":
        await grup.edit("`Bana Oluşturmamı İstediğin Veriyi Seç (Kanal Veya Grup)`")
        return

    if chanl_name =="":
        await grup.edit("`(Kanal Veya Grup)una Vermemi İstediğin İsimi Yaz`")
        return

    if True:
#    if not grup.text[0].isalpha() and grup.text[0] not in ("/", "#", "@", "!"):
        if grup.fwd_from:
            return

        

        if veri == "1":
            try:
                result = await grup.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@FgDc_Bot"],
                    title=chanl_name
                ))

                created_chat_id = result.chats[0].id
                await grup.client(functions.messages.DeleteChatUserRequest(
                    chat_id=created_chat_id,
                    user_id="@FgDc_Bot"
                ))

                result = await grup.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))

                await grup.edit("`{}` Siparişinizi Hazırladım, Sahip. \nGörmek için: [{}]({})".format(chanl_name, chanl_name, result.link))
            except Exception as e:  # pylint:disable=C0103,W0703
                await grup.edit(str(e))

        elif veri == "1" or veri == "2":
            try:
                r = await grup.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                    users=["@FgDc_Bot"],
                    title=chanl_name,

                    about="Burası @FireqanqUserBot Tarafından Kurulmuştur!",

                    megagroup=False if veri == "3" else True

                ))

                created_chat_id = r.chats[0].id

                result = await grup.client(functions.messages.ExportChatInviteRequest(

                    peer=created_chat_id,

                ))

                await grup.edit("`{}` Siparişinizi Hazırladım, Sahip. \nGörmek için: [{}]({})".format(chanl_name, chanl_name, result.link))

            except Exception as e:  # pylint:disable=C0103,W0703

                await grup.edit(str(e))
    else:
        await grup.edit("`Bana Oluşturmamı İstediğin Veriyi Seç (Kanal Veya Grup)`")
        return

CmdHelp('olustur').add_command(
    "olustur", "Kanal Veya Grup Oluşturur", "Örnek .OLUSTUR 1 @FireqanqUserBot").add()