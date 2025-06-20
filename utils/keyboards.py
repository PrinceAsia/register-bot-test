from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

request_contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon raqamini yuborish', request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

request_location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Joylashuvni yuborish', request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)