from aiogram import F, types, Router


group_admin_router = Router()
FORBIDDEN_WORDS = ('дурак', 'баран', 'быдло')


@group_admin_router.message(F.chat.type == 'group')
async def start(message: types.Message):
    for i in FORBIDDEN_WORDS:
        if i in message.text.lower():
            await message.reply(f'{message.from_user.first_name} выгнан из группы за'
                                f'использование оскорбительных выражений')
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id
            )
