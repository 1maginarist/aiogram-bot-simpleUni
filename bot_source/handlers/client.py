from aiogram import types
from create_bot import bot, Dispatcher
from bot_source.keyboards import keyboard_start, keyboard_months, keyboard_remove
from bot_source.other.utilities import get_coinflip_util, get_prediction_util
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from bot_source.filters.filters import date_filter
from bot_source.database import database_schedule


'''*************** Клиентская часть ***************'''


class FSMClient(StatesGroup):
    faculty = State()
    month = State()
    date = State()


# @dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, f'Добро пожаловать, {msg.from_user.username}\nДанный бот - это упрощенная версия личного кабинета СамГТУ',
                           reply_markup=keyboard_start)


# @dp.message_handler(commands=['Подбросить монетку'])
async def get_coinflip(msg: types.Message):
    await bot.send_message(msg.from_user.id, get_coinflip_util())


# @dp.message_handler(commands=['Получить педсказание'])
async def get_prediction(msg: types.Message):
    await bot.send_message(msg.from_user.id, get_prediction_util())


# @dp.message_handler(commands=['Узнать расписание'], state=None)
async def get_schedule(msg: types.Message):
    await FSMClient.faculty.set()
    await msg.reply('Введите вашу группу\nНапример "3иаит7":')


# @dp.message_handler(content_types=['text'], state=FSMClient.faculty)
async def input_faculty(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['faculty'] = msg.text
    await FSMClient.next()
    await msg.reply('Отлично, теперь выберите месяц', reply_markup=keyboard_months)


# @dp.message_handler(content_types=['text'], state=FSMClient.month)
async def input_month(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['month'] = msg.text
        await FSMClient.next()
        await bot.send_message(msg.from_user.id, 'Превосходно, теперь введите дату\nНапример (1, 3, 16)', reply_markup=keyboard_remove)


# @dp.message_handler(content_types=['text'], state=FSMClient.date)
async def input_date(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if not date_filter(data['month'], int(msg.text)):
            await msg.reply('Вы ввели некорректную дату, повторите ввод')
            return

        data['date'] = int(msg.text)

        await state.update_data(data)
        result = await database_schedule.db_read(state)
        await bot.send_message(msg.from_user.id, result)
        await state.finish()


# @dp.message_handler(state="*", commands=['Cancel'])
# @dp.message_handler(Text(equals='Cancel', ignore_case=True), state="*")
async def cancel_handler(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer('Ok')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_coinflip, commands=['Подбросить_монетку'])
    dp.register_message_handler(get_prediction, commands=['Получить_педсказание'])
    dp.register_message_handler(cancel_handler, state="*", commands=['Cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='Cancel', ignore_case=True), state="*")
    dp.register_message_handler(get_schedule, commands=['Узнать_расписание'], state=None)
    dp.register_message_handler(input_faculty, content_types=['text'], state=FSMClient.faculty)
    dp.register_message_handler(input_month, content_types=['text'], state=FSMClient.month)
    dp.register_message_handler(input_date, content_types=['text'], state=FSMClient.date)
