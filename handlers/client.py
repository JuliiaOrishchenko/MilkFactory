from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_client, client_kb
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
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


# @dp.message_handler(commands=['Режим роботи'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт з 8.30 до 22.30, Сб-Нд з 8.30 до 23.00')

# @dp.message_handler(commands=['Місцезнаходження точок видачі'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'м. Харків, вул. Тракторобудівників, 18', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message: types.Message):
    await message.answer(text="Оберіть категорію : ", reply_markup=client_kb.choice)


@dp.callback_query_handler(Text(startswith='menu_'))
async def process_callback_data(call: types.CallbackQuery):
    res = str(call.data.split('_')[1])
    match res:
        case 'pizza':
            await sqlite_db.sql_read(call.message.chat.id, 'Піцца')
        case 'sushi':
            await sqlite_db.sql_read(call.message.chat.id, 'Суші')
        case 'juice':
            await sqlite_db.sql_read(call.message.chat.id, 'Напої')
    await call.message.answer(text='Для повернення у меню вибору: ', reply_markup=client_kb.back_mrk)
    await call.answer()

@dp.callback_query_handler(Text(startswith='back_to_categories'))
async def back_to_categories(call: types.CallbackQuery):
    await call.message.answer(text='Оберіть категорію :', reply_markup=client_kb.choice)
    await call.answer()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Mode'])
    dp.register_message_handler(pizza_place_command, commands=['Place'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])
