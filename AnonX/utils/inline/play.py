import math
import time

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    anonn = math.floor(2*percentage)
    anonnn = math.floor(percentage)

    if 0 < anonn <= 10:
        b = "🎶ㅤ"
    elif 10 < anonn < 20:
        b = "𓆩🎧𓆪ㅤ"
    elif 20 <= anonn < 30:
        b = "🎵ㅤ"
    elif 30 <= anonn < 40:
        b = "📀ㅤ"
    elif 40 <= anonn < 50:
        b = "🎙ㅤ"
    elif 50 <= anonn < 60:
        b = "♨️ㅤ"
    elif 60 <= anonn < 70:
        b = "🎸ㅤ"
    elif 70 <= anonn < 80:
        b = "🥁ㅤ"
    elif 80 <= anonn < 90:
        b = "🎧ㅤ"
    elif 90 <= anonn < 100:
        b = "💿ㅤ"
    elif 100 < anonn < 110:
        b = "🎶ㅤ"
    elif 110 <= anonn < 120:
        b = "𝆹𝅥𝅮ㅤ"
    elif 120 <= anonn < 130:
        b = "𝄞ㅤ"
    elif 130 <= anonn < 140:
        b = "𝅘𝅥𝅯ㅤ"
    elif 140 <= anonn < 150:
        b = "𓆩🎧𓆪ㅤ"
    elif 150 <= anonn < 160:
        b = "𝆹𝅥𝅯ㅤ"
    elif 160 <= anonn < 170:
        b = "🎸ㅤ"
    elif 170 <= anonn < 180:
        b = "🎲ㅤ"
    elif 180 <= anonn < 195:
        b = "𝅘𝅥𝅯ㅤ"
    else:
        b = "𓆩🎧𓆪ㅤ"

    
    
    if 0 < anonn <= 10:
        ba = "ㅤ🎸"
    elif 10 < anonn < 20:
        ba = "ㅤ🎙"
    elif 20 <= anonn < 30:
        ba = "ㅤ𓆩🎧𓆪"
    elif 30 <= anonn < 40:
        ba = "ㅤ𝅘𝅥𝅯"
    elif 40 <= anonn < 50:
        ba = "ㅤ♨️"
    elif 50 <= anonn < 60:
        ba = "ㅤ𝄞"
    elif 60 <= anonn < 70:
        ba = "ㅤ🎲"
    elif 70 <= anonn < 80:
        ba = "ㅤ𝆹𝅥𝅯"
    elif 80 <= anonn < 90:
        ba = "ㅤ🎙"
    elif 90 <= anonn < 100:
        ba = "ㅤ𝄞"
    elif 100 < anonn < 110:
        ba = "ㅤ🎶"
    elif 110 <= anonn < 120:
        ba = "ㅤ💿"
    elif 120 <= anonn < 130:
        ba = "ㅤ🎵"
    elif 130 <= anonn < 140:
        ba = "ㅤ🎸"
    elif 140 <= anonn < 150:
        ba = "ㅤ📀"
    elif 150 <= anonn < 160:
        ba = "ㅤ🎶"
    elif 160 <= anonn < 170:
        ba = "ㅤ𝆹𝅥𝅯"
    elif 170 <= anonn < 180:
        ba = "ㅤ𓆩🎧𓆪"
    elif 180 <= anonn < 195:
        ba = "ㅤ♨️"
    else:
        ba = "ㅤ🎵"





    
    if 0 < anonnn <= 10:
        baa = "☉═════════"
    elif 10 < anonnn < 20:
        baa = "═☉════════"
    elif 20 <= anonnn < 30:
        baa = "══☉═══════"
    elif 30 <= anonnn < 40:
        baa = "═══☉══════"
    elif 40 <= anonnn < 50:
        baa = "════☉═════"
    elif 50 <= anonnn < 60:
        baa = "═════☉════"
    elif 60 <= anonnn < 70:
        baa = "══════☉═══"
    elif 70 <= anonnn < 80:
        baa = "═══════☉══"
    elif 80 <= anonnn < 95:
        baa = "════════☉═"
    else:
        baa = "═════════☉"


#bar of wynk---------------------------------------
    if 0 < anon <= 1:
        bar = "𝐓αιταи 𝐁ιg 𝐃αταϐαѕє "
    elif 1 <= anon < 2:
        bar = "ı.ıllı.ılılıı.ıılı.ılııllı.ılılııı.ıllıı"
    elif 2 <= anon < 3:
        bar = "𝐓αιταи 𝐁ιg 𝐃αταϐαѕє"
    elif 3 <= anon < 4:
        bar = "ı.ıllı.ılılıııılı.ıllı.ılılııı.ıllııılı"
    elif 4 <= anon < 5:
        bar = "𝐓αιταи 𝐌υѕιϲ 𝐋αg 𝐅яєє"
    elif 5 <= anon < 6:
        bar = "lıllılı.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 6 <= anon < 7:
        bar = ".ılılıl.ııllı.ılılııı.ıllııllı.ılılıı"
    elif 7 <= anon < 8:
        bar = "lıllılı.ıllı.ıllı.ılılııı.ıllıı.ılılıı"
    elif 8 <= anon < 9:
        bar = ".ılılıl.ıllı.ııllı.ılılııı.ıllıılılıı"
    elif 9 <= anon < 10:
        bar = "lıllılı.ıllı.ılılıllı.ılılııı.ıllıııı"
    elif 10 <= anon < 11:
        bar = ".ılılıl.ıllı.ılııllı.ıl.ılııı.ıllıılıı"
    elif 11 <= anon < 12:
        bar = "lıllılı.ıllı.ıllı.ılılııı.ıllııılılıı"
    elif 12 <= anon < 13:
        bar = "lıllılı.ıllı.ılıllı.ılılııı.ıllııılıı"
    elif 13 <= anon < 14:
        bar = ".ılılıl.ıllı.ılı.llı.ılıl.ııı.ıllııılıı"
    elif 14 <= anon < 15:
        bar = "lıllılı.ıllı.ılııllı.ılıl.ııı.ıllıılıı"
    elif 15 <= anon < 16:
        bar = "lıllılı.ıllı.ılııllı.ılılııı.ıllıılıı"
    elif 16 <= anon < 17:
        bar = ".ılılıl.ıllı.ılıllı.ılılııı.ıllııılıı"
    elif 17 <= anon < 18:
        bar = "lıllıllı.ılılııı.ıllııılı.ıllı.ılılıı"
    elif 18 <= anon < 19:
        bar = ".ılılıl.ıllııllı.ılılııı.ıllıı.ılılıı"
    elif 19 <= anon < 20:
        bar = "lıllılı.ıllı.ılılıııllı.ılılııı.ıllıı"
    elif 20 <= anon < 21:
        bar = "lıllılı.ıllııllı.ılılııı.ıllıı.ılılıı"
    elif 21 <= anon < 22:
        bar = ".ılılıl.ıllı.ılııllı.ılılııı.ıllıılıı"
    elif 22 <= anon < 23:
        bar = "lıllılı.ıllı.ılııllı.ılılııı.ıllıılıı"
    elif 23 <= anon < 24:
        bar = ".ılılıl.ılıllı.ılılııı.ıllıılı.ılılıı"
    elif 24 <= anon < 25:
        bar = "lıllılı.ıllıllı.ılılııı.ıllııı.ılılıı"
    elif 25 <= anon < 26:
        bar = ".ılılıl.ılıllı.ılılııı.ıllıılı.ılılıı"
    elif 26 <= anon < 27:
        bar = "lıllılı.ılıllı.ılılııı.ıllıılı.ılılıı"
    elif 27 <= anon < 28:
        bar = ".ıllı.ılılııı.ıllıı.ıllı.ılılııı.ıllıı"
    elif 28 <= anon < 29:
        bar = "lıllılı.ılıllı.ılılııı.ıllıılı.ılılıı"
    elif 29 <= anon < 30:
        bar = ".ılılıl.ııllı.ılılııı.ıllııllı.ılılıı"
    elif 30 <= anon < 31:
        bar = "lıllılı.ıllı.ılıllı.ılılııı.ıllııılıı"
    elif 31 <= anon < 32:
        bar = "lıllılı.ıllı.ılıllı.ılılııı.ıllııılıı"
    elif 32 <= anon < 33:
        bar = ".ılılıl.ıllı.ılıllı.ılılııı.ıılıı"
    elif 33 <= anon < 34:
        bar = "lılıllı.ılılııı.ıllıılılı.ıllı.ılılıı"
    elif 34 <= anon < 35:
        bar = "ılıllı.ılılııı.ıllıılılı.ıllı.ılılıı"
    elif 35 <= anon < 36:
        bar = ".ılılıl.ııllı.ılılııı.ıllııllı.ılılıı"
    elif 36 <= anon < 37:
        bar = "lıllılı.ıllı.ıllı.ılılııı.ıllııılılıı"
    elif 37 <= anon < 38:
        bar = ".ıllı.ılılııı.ıllıııllı.ılılııı.ıllıı"
    elif 38 <= anon < 39:
        bar = "lıllılı.ıllı..ıllı.ılılııı.ıllıılılıı"
    elif 39 <= anon < 40:
        bar = ".ılılıl.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 40 <= anon < 41:
        bar = "lıll.ıllı.ılılııı.ıllııılı.ıllı.ılılıı"
    elif 41 <= anon < 42:
        bar = "lıllılı.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 42 <= anon < 43:
        bar = ".ılılıl.ıllı.ıl.ıllı.ılılııı.ıllııılıı"
    elif 43 <= anon < 44:
        bar = "lıllılı.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 44 <= anon < 45:
        bar = "lıllılı.ıllı.ıl.ıllı.ılılııı.ıllııılıı"
    elif 45 <= anon < 46:
        bar = ".ılıl.ıllı.ılılııı.ıllıııl.ıllı.ılılıı"
    elif 46 <= anon < 47:
        bar = "lıllılı.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 47 <= anon < 48:
        bar = "lıllılı.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 48 <= anon < 49:
        bar = ".ılılıl.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 49 <= anon < 50:
        bar = "lıllılı.ıllı.ıl.ıllı.ılılııı.ıllııılıı"
    elif 50 <= anon < 51:
        bar = ".ılı.ıllı.ılılııı.ıllıılıl.ıllı.ılılıı"
    elif 51 <= anon < 52:
        bar = "lıllı.ıllı.ılılııı.ıllıılı.ıllı.ılılıı"
    elif 52 <= anon < 53:
        bar = ".ılılıl.ıllı.ılılı.ıllı.ılılııı.ıllııı"
    elif 53 <= anon < 54:
        bar = "lıllılı.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 54 <= anon < 55:
        bar = "lıllılı.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 55 <= anon < 56:
        bar = ".ılıl.ıllı.ılılııı.ıllıııl.ıllı.ılılıı"
    elif 56<= anon < 57:
        bar = "lıl.ıllı.ılılııı.ıllıılılı.ıllı.ılılıı"
    elif 57 <= anon < 58:
        bar = ".ıllı.ılılııı.ıllıılıllılı.ıllı.ılılıı"
    elif 58 <= anon < 59:
        bar = ".ılı.ıllı.ılılııı.ıllıılıl.ıllı.ılılıı"
    elif 59 <= anon < 60:
        bar = "lıll.ıllı.ılılııı.ıllııılı.ıllı.ılılıı"
    elif 60 <= anon < 61:
        bar = "lıllılı.ıllı.ıl.ıllı.ılılııı.ıllııılıı"
    elif 61 <= anon < 62:
        bar = ".ılılıl.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 62 <= anon < 63:
        bar = "lıllılı.ıllı..ıllı.ılılııı.ıllııılılıı"
    elif 63 <= anon < 64:
        bar = ".ıllı.ılılııı.ıllıılıllılı.ıllı.ılılıı"
    elif 64 <= anon < 65:
        bar = ".ılılıl.ıl.ıllı.ılılııı.ıllıılı.ılılıı"
    elif 65 <= anon < 66:
        bar = "lıllılı.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 66 <= anon < 67:
        bar = ".ıllı.ılılııı.ıllıı.ıllı.ılılııı.ıllıı"
    elif 67 <= anon < 68:
        bar = "lıllılı.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 68 <= anon < 69:
        bar = ".ılılıl.ıllı.ılılııı.ıllıı.ıllı.ılılıı"
    elif 69 <= anon < 70:
        bar = "lıllılı.ıllı.ıl.ıllı.ılılııı.ıllııılıı"
    elif 70 <= anon < 71:
        bar = ".ıllı.ılılııı.ıllıılıllılı.ıllı.ılılıı"
    elif 71 <= anon < 72:
        bar = "ılılıl.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 72 <= anon < 73:
        bar = "lıll.ıllı.ılılııı.ıllııılı.ıllı.ılılıı"
    elif 73 <= anon < 74:
        bar = ".ılılıl.ıllı.ılılıı.ıllı.ılılııı.ıllıı"
    elif 74 <= anon < 75:
        bar = "lıllılı.ıllı.ılılıı.ıllı.ılılııı.ıllıı"
    elif 75 <= anon < 76:
        bar = ".ılılıl.ıllı.ılılıı.ıllı.ılılııı.ıllıı"
    elif 76 <= anon < 77:
        bar = "lıllılı.ıllı.ılılıı.ıllı.ılılııı.ıllıı"
    elif 77 <= anon < 78:
        bar = "lıllılı.ıllı.ılılıı.ıllı.ılılııı.ıllıı"
    elif 78 <= anon < 79:
        bar = ".ılılıl.ıllı.ılılıı.ıllı.ılılııı.ıllıı"
    elif 79 <= anon < 80:
        bar = "lıllılı.ıllı.ılılıı.ıllı.ılılııı.ıllıı"
    elif 80 <= anon < 81:
        bar = "lıllılı.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 81 <= anon < 82:
        bar = ".ılılıl.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 82 <= anon < 83:
        bar = "lıllılı.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 83 <= anon < 84:
        bar = "lıll.ıllı.ılılııı.ıllııılı.ıllı.ılılıı"
    elif 84 <= anon < 85:
        bar = ".ıl.ıllı.ılılııı.ıllııılıl.ıllı.ılılıı"
    elif 85 <= anon < 86:
        bar = "l.ıllı.ılılııı.ıllıııllılı.ıllı.ılılıı"
    elif 86 <= anon < 87:
        bar = ".ılılıl.ıllı.ıl.ıllı.ılılııı.ıllııılıı"
    elif 87 <= anon < 88:
        bar = "lıl.ıllı.ılılııı.ıllıılılı.ıllı.ılılıı"
    elif 88 <= anon < 89:
        bar = ".ılılıl.ıllı.ılıl.ıllı.ılılııı.ıllıııı"
    elif 89 <= anon < 90:
        bar = "lıll.ıllı.ılılııı.ıllııılı.ıllı.ılılıı"
    elif 90 <= anon < 91:
        bar = ".ılılıl.ıllı.ılı.ıllı.ılılııı.ıllıılıı"
    elif 91 <= anon < 92:
        bar = "lıll.ıllı.ılılııı.ıllııılı.ıllı.ılılıı"
    elif 92 <= anon < 93:
        bar = ".ılılıl.ıllı.ıl.ıllı.ılılııı.ıllııılıı"
    elif 93 <= anon < 94:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 94 <= anon < 95:
        bar = "𝐓αιταи ƒяєє мυѕιϲ"
    elif 95 <= anon < 96:
        bar = ".𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 96 <= anon < 97:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 97 <= anon < 98:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 98 <= anon < 99:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"


    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {baa} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{b} {bar} {ba}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/ALONE_WAS_BOT"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐂ᥣⱺ𝗌𝖾", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(2*percentage)
    if 0 < anon <= 10:
        bar = "☉═════════"
    elif 10 < anon < 20:
        ba = "═☉════════"
    elif 20 <= anon < 30:
        ba = "══☉═══════"
    elif 30 <= anon < 40:
        ba = "═══☉══════"
    elif 40 <= anon < 50:
        ba = "════☉═════"
    elif 50 <= anon < 60:
        ba = "═════☉════"
    elif 60 <= anon < 70:
        ba = "══════☉═══"
    elif 70 <= anon < 80:
        ba = "═══════☉══"
    elif 80 <= anon < 95:
        ba = "════════☉═"
    else:
        ba = "═════════☉"

# Wynk bar-----------------------------------------------------------
    if 0 < anon <= 1:
        bar = "lıllılı.ıllı.ılılıı"
    elif 1 <= anon < 2:
        bar = "ı.ıllı.ılılıııılı.ılı"
    elif 2 <= anon < 3:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 3 <= anon < 4:
        bar = "ı.ıllı.ılılıııılı.ılı"
    elif 4 <= anon < 5:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 5 <= anon < 6:
        bar = "lıllılı.ıllı.ılılıı"
    elif 6 <= anon < 7:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 7 <= anon < 8:
        bar = "lıllılı.ıllı.ılılıı"
    elif 8 <= anon < 9:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 9 <= anon < 10:
        bar = "lıllılı.ıllı.ılılıı"
    elif 10 <= anon < 11:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 11 <= anon < 12:
        bar = "lıllılı.ıllı.ılılıı"
    elif 12 <= anon < 13:
        bar = "lıllılı.ıllı.ılılıı"
    elif 13 <= anon < 14:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 14 <= anon < 15:
        bar = "lıllılı.ıllı.ılılıı"
    elif 15 <= anon < 16:
        bar = "lıllılı.ıllı.ılılıı"
    elif 16 <= anon < 17:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 17 <= anon < 18:
        bar = "lıllılı.ıllı.ılılıı"
    elif 18 <= anon < 19:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 19 <= anon < 20:
        bar = "lıllılı.ıllı.ılılıı"
    elif 20 <= anon < 21:
        bar = "lıllılı.ıllı.ılılıı"
    elif 21 <= anon < 22:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 22 <= anon < 23:
        bar = "lıllılı.ıllı.ılılıı"
    elif 23 <= anon < 24:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 24 <= anon < 25:
        bar = "lıllılı.ıllı.ılılıı"
    elif 25 <= anon < 26:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 26 <= anon < 27:
        bar = "lıllılı.ıllı.ılılıı"
    elif 27 <= anon < 28:
        bar = "lıllılı.ıllı.ılılıı"
    elif 28 <= anon < 29:
        bar = "lıllılı.ıllı.ılılıı"
    elif 29 <= anon < 30:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 30 <= anon < 31:
        bar = "lıllılı.ıllı.ılılıı"
    elif 31 <= anon < 32:
        bar = "lıllılı.ıllı.ılılıı"
    elif 32 <= anon < 33:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 33 <= anon < 34:
        bar = "lıllılı.ıllı.ılılıı"
    elif 34 <= anon < 35:
        bar = "lıllılı.ıllı.ılılıı"
    elif 35 <= anon < 36:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 36 <= anon < 37:
        bar = "lıllılı.ıllı.ılılıı"
    elif 37 <= anon < 38:
        bar = "lıllılı.ıllı.ılılıı"
    elif 38 <= anon < 39:
        bar = "lıllılı.ıllı.ılılıı"
    elif 39 <= anon < 40:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 40 <= anon < 41:
        bar = "lıllılı.ıllı.ılılıı"
    elif 41 <= anon < 42:
        bar = "lıllılı.ıllı.ılılıı"
    elif 42 <= anon < 43:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 43 <= anon < 44:
        bar = "lıllılı.ıllı.ılılıı"
    elif 44 <= anon < 45:
        bar = "lıllılı.ıllı.ılılıı"
    elif 45 <= anon < 46:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 46 <= anon < 47:
        bar = "lıllılı.ıllı.ılılıı"
    elif 47 <= anon < 48:
        bar = "lıllılı.ıllı.ılılıı"
    elif 48 <= anon < 49:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 49 <= anon < 50:
        bar = "lıllılı.ıllı.ılılıı"
    elif 50 <= anon < 51:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 51 <= anon < 52:
        bar = "lıllılı.ıllı.ılılıı"
    elif 52 <= anon < 53:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 53 <= anon < 54:
        bar = "lıllılı.ıllı.ılılıı"
    elif 54 <= anon < 55:
        bar = "lıllılı.ıllı.ılılıı"
    elif 55 <= anon < 56:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 56<= anon < 57:
        bar = "lıllılı.ıllı.ılılıı"
    elif 57 <= anon < 58:
        bar = "lıllılı.ıllı.ılılıı"
    elif 58 <= anon < 59:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 59 <= anon < 60:
        bar = "lıllılı.ıllı.ılılıı"
    elif 60 <= anon < 61:
        bar = "lıllılı.ıllı.ılılıı"
    elif 61 <= anon < 62:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 62 <= anon < 63:
        bar = "lıllılı.ıllı.ılılıı"
    elif 63 <= anon < 64:
        bar = "lıllılı.ıllı.ılılıı"
    elif 64 <= anon < 65:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 65 <= anon < 66:
        bar = "lıllılı.ıllı.ılılıı"
    elif 66 <= anon < 67:
        bar = "lıllılı.ıllı.ılılıı"
    elif 67 <= anon < 68:
        bar = "lıllılı.ıllı.ılılıı"
    elif 68 <= anon < 69:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 69 <= anon < 70:
        bar = "lıllılı.ıllı.ılılıı"
    elif 70 <= anon < 71:
        bar = "lıllılı.ıllı.ılılıı"
    elif 71 <= anon < 72:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 72 <= anon < 73:
        bar = "lıllılı.ıllı.ılılıı"
    elif 73 <= anon < 74:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 74 <= anon < 75:
        bar = "lıllılı.ıllı.ılılıı"
    elif 75 <= anon < 76:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 76 <= anon < 77:
        bar = "lıllılı.ıllı.ılılıı"
    elif 77 <= anon < 78:
        bar = "lıllılı.ıllı.ılılıı"
    elif 78 <= anon < 79:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 79 <= anon < 80:
        bar = "lıllılı.ıllı.ılılıı"
    elif 80 <= anon < 81:
        bar = "lıllılı.ıllı.ılılıı"
    elif 81 <= anon < 82:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 82 <= anon < 83:
        bar = "lıllılı.ıllı.ılılıı"
    elif 83 <= anon < 84:
        bar = "lıllılı.ıllı.ılılıı"
    elif 84 <= anon < 85:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 85 <= anon < 86:
        bar = "lıllılı.ıllı.ılılıı"
    elif 86 <= anon < 87:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 87 <= anon < 88:
        bar = "lıllılı.ıllı.ılılıı"
    elif 88 <= anon < 89:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 89 <= anon < 90:
        bar = "lıllılı.ıllı.ılılıı"
    elif 90 <= anon < 91:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 91 <= anon < 92:
        bar = "lıllılı.ıllı.ılılıı"
    elif 92 <= anon < 93:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 93 <= anon < 94:
        bar = "lıllılı.ıllı.ılılıı"
    elif 94 <= anon < 95:
        bar = "lıllılı.ıllı.ılılıı"
    elif 95 <= anon < 96:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 96 <= anon < 97:
        bar = "lıllılı.ıllı.ılılıı"
    elif 97 <= anon < 98:
        bar = ".ılılıl.ıllı.ılılıı"
    elif 98 <= anon < 99:
        bar = "lıllılı.ıllı.ılılıı"
    else:
        bar = ".ılılıl.ıllı.ılılıı"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {ba} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{bar}",
                callback_data="GetTimer",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/ALONE_WAS_BOT"
            ),    
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/ALONE_WAS_BOT"
           ),
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="►►", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
                callback_data=f"add_playlist {videoid}",
            ),
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/taitangamer"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="𝑪𝒍𝒐𝒔𝒆", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            
            InlineKeyboardButton(
                text="❀⋟ 𝐃єνєℓσρєя ⋞❀", url="https://t.me/taitangamer"
            ),
        ],
        [       
            InlineKeyboardButton(
                text="𝑪𝒍𝒐𝒔𝒆", callback_data=f"close"
            )
        ],
    ]
    return buttons
