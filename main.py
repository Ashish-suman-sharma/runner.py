import telebot
from telebot import types

bot = telebot.TeleBot("6750932689:AAHSK1ri1eBTwFv1Caycp9N7vBaFEj89VK0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://Ashishsuman.me") 
    button = types.InlineKeyboardButton("Open Website", web_app=web_app)
    markup.add(button)
    bot.send_message(message.chat.id, "Welcome! Click the button to open the website.", reply_markup=markup)

bot.polling()
