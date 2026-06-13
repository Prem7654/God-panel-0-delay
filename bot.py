import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Need help ?\n\nContact owner - @NonsenseBy"
    )

bot.infinity_polling()
