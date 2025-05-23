import asyncio
import logging
from pyrogram.enums import ChatType, ChatMemberStatus
from zefron import app
from pyrogram import filters
from zefron.utils.RAUSHAN_ban import admin_filter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

SPAM_CHATS = []

@app.on_message(filters.command(["mention", "all"]) & filters.group & admin_filter)
async def tag_all_users(_, message):
    try:
        replied = message.reply_to_message
        if len(message.command) < 2 and not replied:
            await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ**")
            return

        if replied:
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 5
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 1:
                    await replied.reply_text(usertxt)
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            try:
                SPAM_CHATS.remove(message.chat.id)
            except Exception as e:
                logger.error(f"Error removing chat from SPAM_CHATS: {str(e)}")
        else:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await app.send_message(message.chat.id, f'{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /alloff ||')
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            try:
                SPAM_CHATS.remove(message.chat.id)
            except Exception as e:
                logger.error(f"Error removing chat from SPAM_CHATS: {str(e)}")
    except Exception as e:
        logger.error(f"Error in tag_all_users: {str(e)}")
        await message.reply_text("An error occurred while processing your request.")

@app.on_message(filters.command("alloff") & ~filters.private)
async def cancelcmd(_, message):
    try:
        chat_id = message.chat.id
        if chat_id in SPAM_CHATS:
            try:
                SPAM_CHATS.remove(chat_id)
            except Exception as e:
                logger.error(f"Error removing chat from SPAM_CHATS: {str(e)}")
            return await message.reply_text("**ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")
        else:
            await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
            return
    except Exception as e:
        logger.error(f"Error in cancelcmd: {str(e)}")
        await message.reply_text("An error occurred while processing your request.")

if __name__ == "__main__":
    logger.info("Starting bot...")
    app.run()       
