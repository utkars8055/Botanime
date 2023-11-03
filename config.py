import os
import dotenv
from telethon import TelegramClient
from pymongo import MongoClient
from API.gogoanimeapi import Gogo
from pymongo.collection import Collection

dotenv.load_dotenv(".env")

api_id = os.environ.get('25276771')
api_hash = os.environ.get('9b9b4b689989390be2ab0889f0e8e459')
bot_token = os.environ.get('6897949043:AAFJR4a0g7wKydGh0u10v3Ct0uNCRgFNq4A')
db_url = os.environ.get('MONGO_DB_URL')
database_name = os.environ.get('DATABASE_NAME')
owner_id = int(os.environ.get('OWNER_ID'))
bot_username = os.environ.get('Personal_gpt0_bot')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = MongoClient(db_url, tls=True)
data = Collection(client[database_name], 'ConfigDB').find_one({"_id":"GogoAnime"})

gogo = Gogo(
        gogoanime_token=data["gogoanime"],
        auth_token=data["auth"],
        host=data["url"]
    )