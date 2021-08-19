from bot.loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.db.database import DBCommands
from bot.keyboards import main_keyboard
from client.algorithm import main
from client.api import price
from client.config import ASSET

db = DBCommands()


@dp.message_handler(CommandStart())
async def register_user(message: Message):
    user_id = message.from_user.id
    user = await db.add_new_user()
    id = user.id
    text = "Приветствую! Я торговый бот на бирже Binance."
    await bot.send_message(user_id, text, reply_markup=main_keyboard.keyboard)


@dp.callback_query_handler(lambda call: call.data == 'start_trade')
async def callback_message(callback_query: CallbackQuery):
    await callback_query.message.answer("Торговля запущена")
    # Запуск алгоритм из бота
    # START_PRICE = price(ASSET)
    # main(START_PRICE)
