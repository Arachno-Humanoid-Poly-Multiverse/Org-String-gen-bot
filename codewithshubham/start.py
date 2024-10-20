from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ʜᴇʏ {msg.from_user.mention},

ɪ ᴀᴍ {me2},
ᴛʀᴜꜱᴛᴇᴅ ꜱᴛʀɪɴɢ ɢᴇɴʀᴀᴛᴏʀ ʙᴏᴛ.
ꜰᴜʟʟʏ ꜱᴀꜰᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ.
ɴᴏ ᴇʀʀᴏʀ.

ᴍᴀᴅᴇ ʙʏ  : [ᴠʀ ᴜɴʀᴇᴀʟ](https://t.me/vr_support) !""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton("⚡️ ᴍᴜꜱɪᴄ ʙᴏᴛ ⚡️", url="https://t.me/VR_String_Gen_Bot"),
                    InlineKeyboardButton("✨ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✨", url="https://t.me/unreal_X_shubham")
              ],[
                    InlineKeyboardButton(text="ɢᴇɴʀᴀᴛᴇ ꜱᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/vr_support"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/vr_unreal")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
