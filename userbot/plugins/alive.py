import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ANONYMOUS"

# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for MASTERMIND USERBOT
global ghanti
ghanti = borg.uid
edit_time = 3
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/19ea7a05f62940857d2df.jpg"
file2 = "https://telegra.ph/file/7d178738fb18a11eb6c7e.jpg"
file3 = "https://telegra.ph/file/dd324f29c0491b035eaea.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "** Apun Zinda He Sarr ^.^** \n`BOT : ` **☣Hot(Bole toh ekdam garam) **\n\n"
pm_caption += "°•✮•° About My System °•✮•°\n\n"
pm_caption += "➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.15.0\n"
pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/XMASTER_MIND_BOT)\n"
pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [MASTERMIND™](https://github.com/RDX-ANONYMOUS/MASTER-MIND-BOT)\n"
pm_caption += "➾ **𝙲𝙾𝙿𝚈𝚁𝙸𝙶𝙷𝚃 𝙱𝚈** ☞ [𝕄𝔸𝕊𝕋𝔼ℝ 𝕄𝕀ℕ𝔻 𝕌𝕊𝔼ℝ𝔹𝕆𝕋](https://github.com/RDX-ANONYMOUS/MASTER-MIND-BOT)\n\n"
pm_caption += f"➾ **M̸R̸ N̸O̸O̸B̸** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"

@borg.on(admin_cmd(pattern=r"alive"))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)
