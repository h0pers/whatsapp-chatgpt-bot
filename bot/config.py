import os.path
import pytz

from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

load_dotenv(os.path.join(BASE_DIR, '.env'))

REDIS_URL = f'redis://{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}/0'

OPEN_AI_API = os.getenv('OPEN_AI')

OPEN_AI_ASSISTANCE_ID = os.getenv('OPEN_AI_ASSISTANCE_ID')

WHATSAPP_ID = os.getenv('WHATSAPP_ID')

WHATSAPP_API_KEY = os.getenv('WHATSAPP_API_KEY')

WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER')

TIME_ZONE_STR = os.getenv('TIME_ZONE')

TIME_ZONE = pytz.timezone(TIME_ZONE_STR)

OPEN_AI_CLIENT = OpenAI(api_key=OPEN_AI_API)

TASK_LIST = [
    'bot.tasks.send_message',
]
