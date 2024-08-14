import telebot
from telebot import types

bot = telebot.TeleBot("6899288816:AAF61IJ-JcAUH1PcWYZ0g89k-F947FMSMRo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://ashishsuman.me/pepelayer/") 
    button = types.InlineKeyboardButton("Open Website", web_app=web_app)
    markup.add(button)
    bot.send_message(message.chat.id, "Welcome! Click the button to open the website.", reply_markup=markup)

bot.polling()
