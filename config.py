import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram API Credentials
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Bot Configuration
BOT_NAME = os.getenv("BOT_NAME", "ʀᴀᴅʜᴀ ✗ ᴀssɪsᴛᴀɴᴛ") 