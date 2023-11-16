from aiogram import types, F
from aiogram.fsm.context import FSMContext
from utils.statesform import Questions


async def get_form(message: types.Message, state: FSMContext):
    await message.answer(f'Здравствуйте, начинаем опрос. Введите своё имя')
    await state.set_state(Questions.GET_NAME)


async def get_name(message: types.Message, state: FSMContext):
    await message.answer(f'Введите свою фамилию')
    await state.update_data(name=message.text)
    await state.set_state(Questions.GET_LAST_NAME)


async def get_last_name(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Мужской'),
                types.KeyboardButton(text='Женский')
            ]
        ]
    )
    await message.answer('Отлично, выберите ваш пол 👇', reply_markup=kb)
    await state.update_data(last_name=message.text)
    await state.set_state(Questions.GET_GENDER)
    await message.delete_reply_markup()


async def get_gender(message: types.Message, state: FSMContext):
    await message.answer('Отлично, теперь введите любимый сериал')
    await state.update_data(gender=message.text)
    await state.set_state(Questions.GET_FAV_SHOW)


async def get_fav_show(message: types.Message, state: FSMContext):
    await message.answer('Отлично, вы закончили опрос')
    await state.update_data(fav_show=message.text)
    context_data = await state.get_data()
    if context_data.get('gender') == 'Мужской' or context_data.get('gender') == 'Женский':
        pass
    else:
        await message.answer('Введен некорректный пол')  # Проверка
    data_user = f'Ваши данные: \r\n' \
                f'Имя: {context_data.get("name")}\n' \
                f'Фамилия: {context_data.get("last_name")}\n' \
                f'Пол: {context_data.get("gender")}\n' \
                f'Любимый сериал: {context_data.get("fav_show")}\n'
    await message.answer(data_user)
    await state.clear()
