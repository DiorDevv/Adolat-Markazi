from telegram import Bot
from django.conf import settings

# Telegram botga xabar yuborish
def send_message_to_telegram(chat_id, message):
    try:
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=chat_id, text=message)
        print(f"Message sent to {chat_id}")
    except Exception as e:
        print(f"Error sending message: {e}")
