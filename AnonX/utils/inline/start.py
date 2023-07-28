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
                text="нοᴡ το υѕє мє? ϲοммαиᴅ мєиυ.", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 ɢяουᴘ 💥", url=f"https://t.me/BEST_FRIENDS_CHATTIG",
            ),
            InlineKeyboardButton(
                text="🥀 ᴄнαииєʟ 💥", url=f"https://t.me/JAYSHREERAMl1",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ мє το ʏουя gяουρ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ οωиєя ✨",
                url=f"https://t.me/VIP_MAHESH_BABU",
            ),
            InlineKeyboardButton(
                text="💮 ѕουяϲє 💮",
                url=f"https://t.me/taitangamer",
            )
        ],
     ]
    return buttons
