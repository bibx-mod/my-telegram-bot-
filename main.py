import telebot
from config import BOT_TOKEN

# टोकनलाई config.py बाट तानेर बोट इनेबल गर्ने
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "बट रनिन्छ! (ZIP Python Bot is running successfully 🚀)")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "म तपाईंको मसेज पाइरहेको छु, Python ZIP बट अन छ! ✅")

print("PYTHON ZIP BOT STARTED 🚀")
bot.infinity_polling()
