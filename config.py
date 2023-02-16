"""
MusicChatBot, Telegram Video Chat Bot
Copyright (c) 2021  Lisa korea <https://github.com/LISA-KOREA>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "24531402"))
API_HASH = getenv("API_HASH", "0f75926e95a476ccff47dacb52079053")
BOT_TOKEN = getenv("BOT_TOKEN", "5713245787:AAF-x7x7vbxcWO98HFbrkPI8FDIH24iw4Ww")
SESSION_STRING = getenv("SESSION_STRING", "AQCSvnOn3bgp746AsiOPkYnRaTrITjlnYDc6akhXJy3yXWphW6d7ZKXCdy4Zanjg4pOiTinROJdI7HLyhj_EoIX7FVygNoGSLMr6XCTN0VAg0ybiEfA1wFKJHo03o-XBu9t8R3YpO6PE-F8S9nOoY19BmOXnaDW2J6RSe2Igi0DAknblQrdCOASRCvqgoJZ5zWBR26on3zj8LjV4OiL1KiRecn9z99LWD64tCSyE7Q3zF5N902HdIQJ7mJ9m43LDWoldp34ZsAxJBLHQJil2m373sBUq-k48SZUQE_xexmWHHcKv9GfhzCWjXiXbyTkERI1UlGaTpt5ICku8a9t6u8YEAAAAATmlxbUA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "TAMILCHATS_MAKKAL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Alinallmovies")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Prince_of_tele")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1471469091 5117909598").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "Hello Brother Or Sister I'm a group music chat bot to play radio/music/youtube live on telegram group voice chat, not having time to chat with you 🙂!")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
