import json
import logging

from time import sleep
from typing import List, Callable
from datetime import datetime

from bot.utils.request import Requests


class WhatsappBot:
    API_URL = 'https://whatsgate.ru/api/v1/'
    API_KEY = None
    WHATSAPP_ID = None
    WHATSAPP_NUMBER = None
    __request_manager = None
    __HEADERS = None
    __PAYLOAD = None

    def __init__(self, api_key: str, whatsapp_id: str, whatsapp_number: str):
        self.set_api(api_key, whatsapp_id, whatsapp_number)
        self.__request_manager = Requests(url=self.API_URL,
                                          headers=self.__HEADERS,
                                          data=self.__PAYLOAD)

    def get_chats(self):
        return json.dumps(self.__request_manager.post(link_addition='get-chats').json(), ensure_ascii=False)

    def get_private_chats(self) -> List[dict]:
        chats = self.get_chats()
        data = json.loads(chats).get('data')
        private_chats = [chat for chat in data if chat.get('isGroup') is False]
        return private_chats

    def get_events(self, date: datetime = None, action: str = None, page: int = 1, page_cnt: int = 10):
        if date is not None:
            date = date.strftime('%Y-%m-%d %H:%M:%S')

        payload = {
            "date": date,
            'action': action,
            'page_cnt': page_cnt,
            'page': page
        }
        payload.update(self.__PAYLOAD)
        return json.dumps(self.__request_manager.post(link_addition='events-get', data=payload).json(),
                          ensure_ascii=False)

    def get_group_chats(self) -> List[dict]:
        chats = self.get_chats()
        data = json.loads(chats).get('data')
        group_chats = [chat for chat in data if chat.get('isGroup') is True]
        return group_chats

    def send_message(self, recipient_id: str, message: str) -> str:
        payload = {
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "body": message
            }
        }
        payload.update(self.__PAYLOAD)
        return self.__request_manager.post(link_addition='send', data=payload).json()

    def reply_message(self, recipient_id: str, message: str, quote: str) -> str:
        payload = {
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "body": message,
                "quote": quote
            }
        }
        payload.update(self.__PAYLOAD)
        return self.__request_manager.post(link_addition='send', data=payload).json()

    def seen_message(self, recipient_id: str) -> None:
        payload = {
            "recipient": {
                "id": recipient_id
            }
        }
        payload.update(self.__PAYLOAD)
        self.__request_manager.post(link_addition='seen', data=payload).json()

    def set_api(self, api_key: str, whatsapp_id: str, whatsapp_number: str):
        self.set_api_key(api_key)
        self.set_whatsapp_id(whatsapp_id)
        self.set_whatsapp_number(whatsapp_number)
        self.__HEADERS = {
            'Accept': 'application/json',
            'X-API-Key': api_key,
            'Content-Type': 'application/json',
        }
        self.__PAYLOAD = {
            "WhatsappID": whatsapp_id,
        }

    def set_api_key(self, api_key: str, ):
        self.API_KEY = api_key

    def set_whatsapp_id(self, whatsapp_id: str):
        self.WHATSAPP_ID = whatsapp_id

    def set_whatsapp_number(self, whatsapp_number: str):
        self.WHATSAPP_NUMBER = whatsapp_number


class Router:
    tasks: List[Callable] = []

    def __call__(self, *args, **kwargs):
        for task in self.tasks:
            task()

    def add_task(self, task: Callable):
        self.tasks.append(task)

    def add_tasks(self, tasks: List[Callable]):
        for task in tasks:
            self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


class Dispatcher:
    bot = None
    router = None

    def __init__(self, bot: WhatsappBot, router: Router):
        self.router = router
        self.bot = bot

    def start_polling(self):
        while True:
            for task in self.router.tasks:
                task(bot=self.bot)

            sleep(5)
