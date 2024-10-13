from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import asyncio


api = "7391365340:AAFRJbOx8991pgkGy-5xSGh4dGwud302JCI"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
kb.add(button1).add(button2)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, который поможет вам рассчитать ваш возраст и рост в зависимости от вашего веса', reply_markup=kb)

@dp.message_handler(text = 'Рассчитать')
async def set_age(message:types.Message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(state=UserState.age)
async def set_growth(message:types.Message, state:FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message:types.Message, state:FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message:types.Message, state:FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    x = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {x}')

    await state.finish()





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
