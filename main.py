import os
import time
from dotenv import load_dotenv
from internetspeedtwitterbot import InternetSpeedTwitterBot

load_dotenv()

bot = InternetSpeedTwitterBot()

# bot.get_internet_speed()

bot.tweet_at_provider()