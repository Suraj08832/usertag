import logging
from zefron import app
from pyrogram import filters
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
        "• /cancel - Stop tagging process"
    )

if __name__ == "__main__":
    logger.info("Starting bot...")
    app.run() 