from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products, populate_db, add_user, is_included

api = "7892457484:AAEFuhWlWZzQ7GAVZepK5ejaMDjrhJ5g--k"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создание базы данных и заполнение ее начальными данными
initiate_db()
populate_db()

# Обычная клавиатура
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Купить')
button4 = KeyboardButton('Регистрация')
kb.add(button1).add(button2).add(button3).add(button4)

# Inline клавиатура для расчёта калорий
inline_kb_calories = InlineKeyboardMarkup()
inline_button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
inline_button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_kb_calories.add(inline_button_calories, inline_button_formulas)

# Inline клавиатура для продуктов
inline_kb_products = InlineKeyboardMarkup()
inline_kb_products = InlineKeyboardMarkup(row_width=4)

for i in range(1, 5):
    inline_button = InlineKeyboardButton(f'Product{i}', callback_data='product_buying')
    inline_kb_products.add(inline_button)


#Блок работы с товарами и взаимодействием с пользователем(морда бота)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, который поможет вам рассчитать ваш возраст и рост в зависимости от вашего веса', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb_calories)

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()
    products = products[:4]


    for product in products:
        product_id, title, description, price = product
        product_description = f'Название: {title} | Описание: {description} | Цена: {price}'
        with open(f'product{product[0]}.jpg', 'rb') as img:
            if product_id > 4:
                continue
        inline_button = InlineKeyboardButton(text=title, callback_data=f'product_buying_{product_id}')
        inline_kb_products.add(inline_button)


        # Изображение продукта
        await message.answer_photo(photo=open(f'product{product[0]}.jpg', 'rb'))
        await message.answer(product)

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_kb_products)

#Блок работы с пользователями(более продвинутая морда бота)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(text='Регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text

    # Проверяем, существует ли пользователь
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    data = await state.get_data()
    username = data['username']
    email = data['email']


    add_user(username, email, age)
    await message.answer("Вы успешно зарегистрированы!")

    await state.finish()



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
