import json
import logging
from datetime import datetime, timedelta

from bot.bot import WhatsappBot
from bot.config import TIME_ZONE
from bot.tasks.send_message import send_assistance_answer


def new_message(bot: WhatsappBot):
    messages = json.loads(bot.get_events(date=datetime.now(tz=TIME_ZONE) - timedelta(hours=0, minutes=0, seconds=5),
                                         action='message'))
    for message in messages['data']:
        from_user = message['event_data']['message']['from']
        text = message['event_data']['message']['body']
        send_assistance_answer.delay(from_user, text)
