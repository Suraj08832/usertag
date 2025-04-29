from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

async def admin_check(_, __, message):
    if message.chat.type in ["group", "supergroup"]:
        member = await message.chat.get_member(message.from_user.id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    return False

admin_filter = filters.create(admin_check) 