from aiogram.utils.callback_data import CallbackData

from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_client, client_kb
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db


# @dp.message_handler(commands='start')
async def command_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            f'Вітаємо, {message.from_user.first_name}! Цей бот допоможе \
            Вам зробити замовлення піци та суші',
            reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Спілкування з ботом через особисті повідомлення. Напишіть йому: \
                             \nhttps://t.me/Milk_FactoryBot')


# @dp.message_handler(lambda message: message.text == 'Режим роботи')
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт з 8.30 до 22.30, Сб-Нд з 8.30 до 23.00')


# @dp.message_handler(lambda message: message.text == 'Місцезнаходження')
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'м. Харків, вул. Тракторобудівників, 18',
                           reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(lambda message: message.text == 'Меню')
async def pizza_menu_command(message: types.Message):
    await message.answer(text="Оберіть категорію : ", reply_markup=client_kb.choice)


cb = CallbackData('btn', 'type', 'product_name', 'price')


@dp.callback_query_handler(Text(startswith='menu_'))
async def process_callback_data(call: types.CallbackQuery):
    category = call.data.split('_')[1]
    categories = {'pizza': 'Піцца', 'sushi': 'Суші', 'juice': 'Напої'}
    products = await sqlite_db.get_products(categories[category])
    for product in products:
        photo_url, name, description, category, price = product
        caption = f'{name}\nОпис: {description}\nЦіна: {price}'
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(text='Замовити', callback_data=f'btn:buy:{name}:{price}'))
        await bot.send_photo(call.message.chat.id, photo_url, caption, reply_markup=keyboard)
    await call.message.answer(text='Інша категорія: ', reply_markup=client_kb.back_mrk)
    await call.answer()


@dp.callback_query_handler(cb.filter(type='buy'))
async def add_to_cart(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=30)

    user_id = call.message.chat.id
    product_name = callback_data.get('product_name')
    price = callback_data.get('price')
    print(f"user_id: {user_id}, product_name: {product_name}, price: {price}")
    await sqlite_db.add_to_cart(user_id, product_name, price)
    await call.message.answer('Додано в корзину')


@dp.callback_query_handler(Text(startswith='back_to_categories'))
async def back_to_categories(call: types.CallbackQuery):
    await call.message.answer(text='Оберіть категорію :', reply_markup=client_kb.choice)
    await call.answer()


@dp.message_handler(lambda message: message.text == 'Ваше замовлення')
async def cart_button_handler(message: types.Message):
    cart_items = await sqlite_db.get_cart(user_id=message.chat.id)
    cart_text = ["{0} {1},00 грн ".format(item[2], item[3]) for item in cart_items]
    if cart_items:
        s = await sqlite_db.cart_get_sum()
        await message.answer("Ваше замовлення:\n" + "\n".join(cart_text) + "\nЗагальна вартість " + s + ",00 грн")
    else:
        await message.answer('Ви ще нічого не замовили')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, lambda message: message.text == 'Режим роботи')
    dp.register_message_handler(pizza_place_command, lambda message: message.text == 'Місцезнаходження')
    dp.register_message_handler(pizza_menu_command, lambda message: message.text == 'Меню')
