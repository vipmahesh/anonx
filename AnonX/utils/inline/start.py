from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "https://t.me/timepassgroup01")
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "https://t.me/dangerous_fighter_clan_0")
OWNER_USERNAME = getenv("OWNER_USERNAME", "https://t.me/taitangamerz")
OWNER_USERNAME = getenv("OWNERR_USERNAME", "https://t.me/taitangamer")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ 𝐀ᴅᴅ 𝐌ᴇ 𝐌ᴏɪ 𝐋ᴜᴠ✚",
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
                text="💔 𝐌u𝐉є 𝐀dd 𝐊α𝐑𝐋σ 𝐁αв𝐘 💔",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝐌ᴀɴᴛᴀɪɴᴇR ✨", url=f"https://t.me/taitangamer",
            ),
            InlineKeyboardButton(
                text="📝 𝐂σmmαn𝐃 𝐃є𝐊𝐋σ 𝐁αв𝐘 📝", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐆ʀᴏᴜ𝐏 💥", url=f"https://t.me/BES_BUDDIES_IN_LIFE",
            ),
            InlineKeyboardButton(
                text="🥀 𝐂ʜᴀɴɴᴇ𝐋 💥", url=f"https://t.me/JAYSHREERAMl",
            )
        ],
        [
            InlineKeyboardButton(
                text="😏 𝐄s𝐊α 𝐁σ𝐓 😏",
                url=f"https://t.me/VIP_MAHESH_BABU",
            )
        ],
     ]
    return buttons
