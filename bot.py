from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Купить')
        ],
        [ KeyboardButton(text='Информация') ]
    ], resize_keyboard=True
)

kb_in = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
b2 = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
kb_in.add(b1)
kb_in.add(b2)

products_buy = InlineKeyboardMarkup()
p1 = InlineKeyboardButton(text = 'Product1', callback_data='buy')
p2 = InlineKeyboardButton(text = 'Product2', callback_data='buy')
p3 = InlineKeyboardButton(text = 'Product3', callback_data='buy')
p4 = InlineKeyboardButton(text = 'Product4', callback_data='buy')
products_buy.add(p1,p2,p3,p4)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('(weight * 10 + 6.425 * growth - 5 * age + 5) * 1.55')
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Купить')
async def buying(message):
    for i in range(4):
        await message.answer(f'Product{i+1}, Описание: описание{i+1}, Цена: {(i+1)*23}')
        with open(f'png{1}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выбери продукт для покупки', reply_markup=products_buy)

@dp.callback_query_handler(text='buy')
async def send_confign_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст.')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост.')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес.')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    await message.answer(f'Ваши параметры: {data}')
    func = float((data["weight"] * 10 + 6.425 * data["growth"] - 5 * data["age"] + 5) * 1.55)
    await message.answer(f'Ваша суточная норма калорий: {func}')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
