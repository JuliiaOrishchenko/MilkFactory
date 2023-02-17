from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup

mode_btn = KeyboardButton('Режим роботи')
place_btn = KeyboardButton('Місцезнаходження')
men_btn = KeyboardButton('Меню')
cart_btn = KeyboardButton('Ваше замовлення')

# start_btn = KeyboardButton('Start')
# start_kb = ReplyKeyboardMarkup(keyboard=start_btn, resize_keyboard=True, selective=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

choice = InlineKeyboardMarkup(row_width=3)
pizza = InlineKeyboardButton(text='🍕 Піцца', callback_data='menu_pizza')
choice.insert(pizza)
sushi = InlineKeyboardButton(text='🍣 Суші', callback_data='menu_sushi')
choice.insert(sushi)
juices = InlineKeyboardButton(text='🥤 Напої', callback_data='menu_juice')
choice.insert(juices)

back_mrk = InlineKeyboardMarkup(row_width=1)
back_btn = InlineKeyboardButton(text='🔙 Назад', callback_data='back_to_categories')
back_mrk.add(back_btn)

kb_client.add(men_btn).insert(cart_btn).add(mode_btn).insert(place_btn)
