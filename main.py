from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from deep_translator import GoogleTranslator
import asyncio

async def start_fun(update: Update, context):
    buttons = [
        [KeyboardButton(text="uz-ru"), KeyboardButton(text="ru-uz")],
        [KeyboardButton(text="uz-en"), KeyboardButton(text="en-uz")]
    ]
    await update.message.reply_text("TARJIMON", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))

async def translate_text(update: Update, context):
    text = update.message.text
    if "-" in text:
        src, dest = text.split("-")
        context.user_data["src"] = src
        context.user_data["dest"] = dest
        await update.message.reply_text(f"Til tanlandi: {src.upper()} → {dest.upper()}.\nEndi matn kiriting:")
    else:
        src = context.user_data.get("src", "auto")
        dest = context.user_data.get("dest", "en")
        translator = GoogleTranslator(source=src, target=dest)
        translation = translator.translate(text)
        await update.message.reply_text(f"Tarjima: {translation}")

TOKEN = "7851854889:AAGyyEWL6NUepspGZOedHHAsI0dpAE1fdX8"

application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start_fun))
application.add_handler(MessageHandler(filters.TEXT, translate_text))
application.run_polling()


