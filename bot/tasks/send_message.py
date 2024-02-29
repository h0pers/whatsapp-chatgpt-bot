from bot.bot import WhatsappBot
from bot.celery import app
from bot.config import WHATSAPP_ID, WHATSAPP_API_KEY, WHATSAPP_NUMBER
from bot.utils.openai_assistance import assistance_answer


@app.task()
def send_assistance_answer(recipient_id: str, incoming_message: str):
    whatsapp_bot = WhatsappBot(whatsapp_id=WHATSAPP_ID, api_key=WHATSAPP_API_KEY, whatsapp_number=WHATSAPP_NUMBER)
    assistance_response = assistance_answer(incoming_message)
    whatsapp_bot.send_message(recipient_id=recipient_id, message=assistance_response)
