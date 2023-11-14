from aiogram import Router, F, types


about_router = Router()


@about_router.callback_query(F.data == 'about')
async def about(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Мы - творческая компания, стремящаяся '
                                  'делать мир лучше через инновации '
                                  'и вдохновение')
