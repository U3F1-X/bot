import telebot

# ضع هنا توكن البوت الخاص بك
API_TOKEN = '7329942132:AAEu2S1qMpwxOHdKF5KlAmzhulHJLQ7YKOs'

# إنشاء كائن البوت
bot = telebot.TeleBot(API_TOKEN)

# عند استقبال رسالة نصية
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا! كيف يمكنني مساعدتك؟")

# عند استقبال أي رسالة نصية أخرى
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# تشغيل البوت
bot.polling()

