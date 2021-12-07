import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Image-Search-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://apibu.herokuapp.com/api/y-images?query="

START_TEXT = """Hello {},
I am an image search bot. You can use me in inline.

Made by @FayasNoushad"""

@Bot.on_message(
    filters.private &
    filters.command(["start"])
)
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def filter_text(bot, update):
    await update.reply_text(
        text=f"Click the button below for searching your query.\n\nQuery: `{update.text}`",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Search Here", switch_inline_query_current_chat=update.text)],
                [InlineKeyboardButton(text="Search in another chat", switch_inline_query=update.text)]
            ]
        ),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_inline_query()
async def search(bot, update):
    results = requests.get(API + requote_uri(update.query)).json()["result"][:50]
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query.lower().capitalize(),
                description=result,
                caption="Made by @FayasNoushad",
                photo_url=result
            )
        )
    await update.answer(answers)


Bot.run()
