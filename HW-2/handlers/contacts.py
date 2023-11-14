from aiogram import Router, F, types


contacts_router = Router()


@contacts_router.callback_query(F.data == 'contacts')
async def contacts(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('''Связаться с нами: 

<b>+996555000810</b>
<b>+996777125112</b>''', parse_mode='HTML')