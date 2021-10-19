import os
import time
from pathlib import Path

import logging
import configparser
import json

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")
# Присваиваем значения внутренним переменным
BOT_API_TOKEN = str(config.get('telegram', 'BOT_API_TOKEN'))

from datetime import datetime, timedelta
import pytz
utc=pytz.UTC

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)