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
API_ID = int(getenv("API_ID", "18286764"))
API_HASH = getenv("API_HASH", "f88e25386cd833a66d15a08d6bc30351")
BOT_TOKEN = getenv("BOT_TOKEN", "5920443941:AAG1UJMR9X7QvM-wUH617Bz8pU-MRqlpM8E")
SESSION_STRING = getenv("SESSION_STRING", "BQEXCKwAXqk4HhKtxCM9Wo6moGonHQEMdG1e5uSZByeNwrPm_HMoQoeCCArFJF4PLbPqp5NPlKNVeaaSHQktG7yAiwGIiH2IqC6Dpeq0teJ7gc9TLGYhVViNW__Nrgj-Y20XCFdwst2XTqYCo_9vFJZ1pooyxA9hciA5in-kXe_OpZi4V5sznsesSh-kN0-As-_AYUmsX6GkTYmDfmpYxA1Xll5eBnQ17R56gteyguRb3f8O8in3Dv-VvBRVyAHioa33BW8-FJlBkJcO7hv5U9VjhT403uWyjkzqc5dBOYcAl8Kz-gEZn4Qcu7alf8_T9GRoWC0weZO0uJ0Bsp-JL2ZPhIXJKQAAAAExDRpeAA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "TAMILCHATS_MAKKAL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Alinallmovies")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1471469091 5117909598").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "Hello Brother Or Sister I'm a group music chat bot to play radio/music/youtube live on telegram group voice chat, not having time to chat with you 🙂!")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
