from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup()
start_btn = InlineKeyboardButton("Начать торговлю", callback_data="start_trade")
keyboard.add(start_btn)
