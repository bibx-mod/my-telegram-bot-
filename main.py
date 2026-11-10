import telebot
from config import BOT_TOKEN

# टोकन लोड गरेर बोट स्टार्ट गर्ने
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "बट रनिन्छ! (GitHub Python Bot is running successfully 🚀)")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "म तपाईंको मसेज पाइरहेको छु, GitHub बाट बट अन छ! ✅")

print("GITHUB PYTHON BOT STARTED 🚀")
bot.infinity_polling()
