from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7391365340:AAFRJbOx8991pgkGy-5xSGh4dGwud302JCI"
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

# @dp.message_handler(text = ['Urban', 'ff'])
# async def urban_message(message):
#     print('Urban message')
#
# @dp.message_handler(commands=['start'])
# async def start_message(message):
#     print('Start message')
#
# @dp.message_handler()
# async def all_mesaages(message):
#     print('Мы получили сообщение')


