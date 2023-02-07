from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

from keyboards.callback_datas import menu_callback

b1 = KeyboardButton('/Mode')
b2 = KeyboardButton('/Place')
b3 = KeyboardButton('/Menu')
inline_btn_1 = InlineKeyboardButton('Молоко', callback_data='b1')
# b4 = KeyboardButton('/Поділитись контактом', request_contact=True)
# b5 = KeyboardButton('/Поділитись місцезнаходженням', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Молоко, кефір", callback_data=menu_callback.new(
#                 item_name='молоко', quantity=2
#             )),
#             InlineKeyboardButton(text="Каші, соки", callback_data="menu:kashi:5"),
#         ],
#         [
#             InlineKeyboardButton(text="Відміна", callback_data="cancel")
#         ]
#     ]
# )

choice = InlineKeyboardMarkup(row_width=2)
milk = InlineKeyboardButton(text='Молоко, кефір', callback_data=menu_callback.new(
                item_name='молоко', quantity=2
        ))
choice.insert(milk)
kashi = InlineKeyboardButton(text='Каші, соки', callback_data=menu_callback.new(
                item_name='каші', quantity=5
        ))
choice.insert(kashi)

cancel_btn = InlineKeyboardButton(text="Відміна", callback_data="cancel")
choice.insert(cancel_btn)

kb_client.add(b1).add(b2).insert(b3)#.row(b4, b5)