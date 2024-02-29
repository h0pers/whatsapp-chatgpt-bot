from celery import Celery
from celery.utils.log import get_task_logger

from bot.config import TIME_ZONE_STR, TASK_LIST, REDIS_URL

app = Celery('bot_celery', broker=REDIS_URL)
app.autodiscover_tasks(TASK_LIST)
app.conf.timezone = TIME_ZONE_STR
logger = get_task_logger(__name__)
