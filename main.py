
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "سلام! به آرشیو موسیقی خوش اومدی 🎵\nبرای دریافت آهنگ، شماره آن را بفرست."
    )

@bot.message_handler(func=lambda message: True)
def receive(message):
    bot.reply_to(message, "هنوز آهنگی به آرشیو اضافه نشده است.")

bot.infinity_polling()
