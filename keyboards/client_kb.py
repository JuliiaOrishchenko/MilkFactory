from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Mode')
b2 = KeyboardButton('/Place')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('/Поділитись контактом', request_contact=True)
# b5 = KeyboardButton('/Поділитись місцезнаходженням', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)#.row(b4, b5)