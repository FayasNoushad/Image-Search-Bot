# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Yandex-Image-Search-Bot/blob/main/LICENSE

import os
from pyrogram import Client, filters


Bot = Client(
    "Yandex-Image-Search-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://apibu.herokuapp.com/api/y-images?query="


@Client.on_inline_query()
async def search(bot, update):
    data = update.data


Bot.run()
