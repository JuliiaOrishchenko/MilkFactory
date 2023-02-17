from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

b1 = KeyboardButton('/Mode')
b2 = KeyboardButton('/Place')
b3 = KeyboardButton('/Menu')
cart_btn = KeyboardButton('/Cart')

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

buy = InlineKeyboardMarkup()
buy_btn = InlineKeyboardButton(text='Купити', callback_data='buy')
buy.add(buy_btn)

kb_client.add(b3).insert(cart_btn).add(b1).insert(b2)


