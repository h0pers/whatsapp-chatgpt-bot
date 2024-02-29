import json
import logging
from datetime import datetime, timedelta

from bot.bot import WhatsappBot
from bot.tasks.send_message import send_assistance_answer


def new_message(bot: WhatsappBot):
    messages = json.loads(bot.get_events(datetime.now() - timedelta(hours=0, minutes=0, seconds=15)))
    for message in messages['data']:
        if message['event_data'].get('message'):
            from_user = message['event_data']['message']['from']
            text = message['event_data']['message']['body']
            send_assistance_answer.delay(from_user, text)
