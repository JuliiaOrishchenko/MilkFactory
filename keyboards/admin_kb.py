from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

# кнопки клавиатуры админа
button_load = KeyboardButton('/Download')
button_delete = KeyboardButton('/Delete')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)

category_btn = InlineKeyboardMarkup(row_width=3)
pizza_category_btn = InlineKeyboardButton('Піцца', callback_data='pizza_category')
sushi_category_btn = InlineKeyboardButton('Суші', callback_data='sushi_category')
juice_category_btn = InlineKeyboardButton('Соки', callback_data='juice_category')

category_btn.add(pizza_category_btn).add(sushi_category_btn).add(juice_category_btn)