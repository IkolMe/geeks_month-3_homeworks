from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='Адрес', callback_data='address'
                ),
                types.InlineKeyboardButton(
                    text='Контакты', callback_data='contacts'
                ),
                types.InlineKeyboardButton(
                    text='О нас', callback_data='about'
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='Наш магазин', callback_data='shop'
                ),
                types.InlineKeyboardButton(
                    text='Наш сайт', url='https://google.com'
                )
            ]
        ]
    )
    await message.answer(
        f'Здравствуйте, {message.from_user.first_name}! Выберите действие 👇',
        reply_markup=kb
    )


@start_router.callback_query(F.data == 'shop')
async def shop(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Продукты питания'),
                types.KeyboardButton(text='Здоровье и спорт')
            ],
            [
                types.KeyboardButton(text='Дом и хозяйство'),
                types.KeyboardButton(text='Путешествия')
            ],
            [
                types.KeyboardButton(text='Бытовые техника'),
                types.KeyboardButton(text='Другое')
            ]
        ]
    )

    msg = await callback.message.answer(
        'Выберите категорию',
        reply_markup=kb
    )


@start_router.message(F.text == 'Продукты питания')
async def food(message: types.Message):
    await message.answer('Вы выбрали категорию "Продукты питания"')


@start_router.message(F.text == 'Здоровье и спорт')
async def food(message: types.Message):
    await message.answer('Вы выбрали категорию "Здоровье и спорт"')


@start_router.message(F.text == 'Дом и хозяйство')
async def food(message: types.Message):
    await message.answer('Вы выбрали категорию "Дом и хозяйство"')


@start_router.message(F.text == 'Путешествия')
async def food(message: types.Message):
    await message.answer('Вы выбрали категорию "Путешествия"')


@start_router.message(F.text == 'Бытовые техника')
async def food(message: types.Message):
    await message.answer('Вы выбрали категорию "Бытовые техника"')


@start_router.message(F.text == 'Другое')
async def food(message: types.Message):
    await message.answer('Вы выбрали категорию "Другое"')
