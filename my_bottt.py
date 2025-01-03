from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "7931711383:AAE1jf7EhEVROJ1zKAPF42NgyUm3jftEEZ0"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Рассчитать')
b2 = KeyboardButton(text='Информация')
kb.add(b1)
kb.add(b2)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()


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
