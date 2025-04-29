import logging
import sys
import os
from zefron import app
from pyrogram import filters
from pyrogram.enums import ChatType, ChatMemberStatus
from config import BOT_NAME

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import all modules
import mention
import gntag
import hitag
import shayari
import tagall

# Start command handler
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        f"Hello! I'm {BOT_NAME}. Here are my commands:\n\n"
        "• /mention or /all - Tag all users\n"
        "• /gn - Good night tag\n"
        "• /hi - Hello tag\n"
        "• /shayari - Shayari tag\n"
        "• /tagall - General tag\n"
        "• /cancel - Stop tagging process\n"
        "• /restart - Restart the bot"
    )

# Restart command handler
@app.on_message(filters.command("restart"))
async def restart_command(client, message):
    try:
        # Check if user is admin
        is_admin = False
        try:
            participant = await client.get_chat_member(message.chat.id, message.from_user.id)
        except:
            is_admin = False
        else:
            if participant.status in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER
            ):
                is_admin = True
        
        if not is_admin:
            return await message.reply("**You are not an admin. Only admins can restart the bot.**")
        
        # Send restart message
        await message.reply("**Restarting bot...**")
        
        # Restart the bot
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    except Exception as e:
        await message.reply(f"**An error occurred while restarting: {str(e)}**")

if __name__ == "__main__":
    logger.info("Starting bot...")
    app.run() 