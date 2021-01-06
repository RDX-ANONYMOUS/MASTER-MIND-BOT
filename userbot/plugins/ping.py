from telethon import events
from datetime import datetime


@command(pattern=".ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("⚠️PONG⚠️")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("⚠️ YOUR PING FOR MASTERMIND USERBOT IS⚠️ \n{}".format(ms))
