# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Yandex-Image-Search-Bot/blob/main/LICENSE

import os
import requests
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Yandex-Image-Search-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://apibu.herokuapp.com/api/y-images?query="


@Bot.on_inline_query()
async def search(bot, update):
    results = requests.get(API + update.query).json()["result"][30:]
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                photo_url=result
            )
        )
    await update.answer(answers)


Bot.run()
