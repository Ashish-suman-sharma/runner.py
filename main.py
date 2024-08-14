import telebot
from telebot import types

bot = telebot.TeleBot("6899288816:AAF61IJ-JcAUH1PcWYZ0g89k-F947FMSMRo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://ashishsuman.me/pepelayer/")
    button = types.InlineKeyboardButton("Open Website", web_app=web_app)
    markup.add(button)
    bot.send_message(message.chat.id, 
        "🎉 Welcome to Pepe Layer 2! 🎉\n\n"
        "💰 Start mining coins now! Tap the big logo to collect coins and complete tasks to earn more.\n\n"
        "🔗 Refer & Earn: Share your referral link and earn rewards when friends join!\n\n"
        "✨ Explore:\n\n"
        "• Home: Track your progress\n"
        "• Tasks: Earn extra coins\n"
        "• Refer & Earn: Share and earn", 
        reply_markup=markup)

bot.polling()
