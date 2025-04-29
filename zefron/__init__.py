import logging
from pyrogram import Client

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    # Initialize the app
    app = Client(
        "zefron_bot",
        api_id="26073471",
        api_hash="eacb2073f9465088e45f65ca6cee5993",
        bot_token="7666194736:AAEyTmsC0sZtHAAjlGxQ0cikRYUtYWlmCRw"
    )
    logger.info("Bot client initialized successfully")
except Exception as e:
    logger.error(f"Error initializing bot: {str(e)}")
    raise 