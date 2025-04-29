import os
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME

# Initialize the bot
app = Client(
    BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start command handler
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(f"Hello! I'm {BOT_NAME}. How can I help you?")

# Run the bot
if __name__ == "__main__":
    print(f"Starting {BOT_NAME}...")
    app.run() 