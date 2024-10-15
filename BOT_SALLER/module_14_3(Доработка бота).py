from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = "7391365340:AAFRJbOx8991pgkGy-5xSGh4dGwud302JCI"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Обычная клавиатура
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Купить')
kb.add(button1).add(button2).add(button3)

# Inline клавиатура для расчёта калорий
inline_kb_calories = InlineKeyboardMarkup()
inline_button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
inline_button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_kb_calories.add(inline_button_calories, inline_button_formulas)

# Inline клавиатура для продуктов
inline_kb_products = InlineKeyboardMarkup()
for i in range(1, 5):
    inline_button = InlineKeyboardButton(f'Product{i}', callback_data='product_buying')
    inline_kb_products.add(inline_button)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, который поможет вам рассчитать ваш возраст и рост в зависимости от вашего веса', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb_calories)

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products_info = []
    for i in range(1, 5):
        product_description = f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}'
        products_info.append(product_description)

        #изображение продукта
        await message.answer_photo(photo=open(f'product{i}.jpg', 'rb'))
        await message.answer(product_description)

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_kb_products)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора: \n"
                              "Для мужчин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n"
                              "Для женщин: BMR = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161")
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    x = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {x}')

    await state.finish()

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
