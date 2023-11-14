from aiogram import Router, F, types


address_router = Router()


@address_router.callback_query(F.data == 'address')
async def address(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Мы находимся на улице Вишневка 152')
