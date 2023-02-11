from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

b1 = KeyboardButton('/Mode')
b2 = KeyboardButton('/Place')
b3 = KeyboardButton('/Menu')
# inline_btn_1 = InlineKeyboardButton('Молоко', callback_data='b1')
# b4 = KeyboardButton('/Поділитись контактом', request_contact=True)
# b5 = KeyboardButton('/Поділитись місцезнаходженням', request_location=True)

start_btn = KeyboardButton('Start')
start_kb = ReplyKeyboardMarkup(keyboard=start_btn, resize_keyboard=True, selective=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)


choice = InlineKeyboardMarkup(row_width=3)
pizza = InlineKeyboardButton(text='Піцца', callback_data='menu_pizza')
choice.insert(pizza)
sushi = InlineKeyboardButton(text='Суші', callback_data='menu_sushi')
choice.insert(sushi)
juices = InlineKeyboardButton(text='Соки', callback_data='menu_juice')
choice.insert(juices)

back_mrk = InlineKeyboardMarkup(row_width=1)
back_btn = InlineKeyboardButton(text='Назад', callback_data='back_to_categories')
back_mrk.add(back_btn)


kb_client.add(b1).add(b2).insert(b3)