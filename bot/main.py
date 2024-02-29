import logging
import sys

from bot.bot import WhatsappBot, Dispatcher, Router
from bot.config import WHATSAPP_ID, WHATSAPP_API_KEY, WHATSAPP_NUMBER
from bot.handlers.new_message import new_message

whatsapp_bot = WhatsappBot(whatsapp_id=WHATSAPP_ID, api_key=WHATSAPP_API_KEY, whatsapp_number=WHATSAPP_NUMBER)


def start_bot():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    router = Router()
    router.add_task(new_message)
    dp = Dispatcher(whatsapp_bot, router)
    dp.start_polling()
