from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀dd 𝐓αɪᴛαи 𝐌υ𝗌𝗂ç 𝐈𐓣 𝐆ʀσup",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑯𝒆𝒍𝒑",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝑺𝒆𝒕𝒕𝒊𝒏𝒈𝒔", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀dd 𝐓αɪᴛαи 𝐌υ𝗌𝗂ç 𝐈𐓣 𝐆ʀσup",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" 𝑯𝒆𝒍𝒑 ", callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐓αɪᴛαи 𝐌υ𝗌𝗂ç", url=f"https://music.apple.com/"
            )
        ],
     ]
    return buttons
