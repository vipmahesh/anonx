from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "")
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 𝐅ᴇᴀᴛᴜʀᴇ 🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️ 𝐒ᴇᴛᴛɪɴɢ ⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝐀ɴᴏᴛʜᴇʀ ✨", url=f"https://t.me/TAITANXMUSICC_BOT",
            ),
            InlineKeyboardButton(
                text="🔎 𝐇ᴇʟᴘ 🔎", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💫 𝐒ᴜᴘᴘᴏʀᴛ 💫", url=f"https://t.me/THEYSTOPPAGE",
            ),
            InlineKeyboardButton(
                text="🍁 𝐔ᴘᴅᴀᴛᴇs 🍁", url=f"https://t.me/taitanoffice",
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ ︎𝐎ᴡɴᴇʀ ♕︎",
                url=f"https://t.me/VIPHerosmart",
            )
        ],
     ]
    return buttons
