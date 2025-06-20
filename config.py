from os import getenv

from dotenv import load_dotenv

from utils.database import Database

load_dotenv()

BOT_TOKEN = getenv("TOKEN")
DB_NAME = getenv("DB_NAME")

db = Database(DB_NAME)
