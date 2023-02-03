from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, f'Вітаємо, {message.from_user.first_name}! Цей бот допоможе \
                               Вам зробити замовлення продуктів дитячого харчування', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Спілкування з ботом через особисті повідомлення. Напишіть йому: \
                            \nhttps://t.me/Milk_FactoryBot')

# @dp.message_handler(commands=['Режим роботи'])
async def milk_factory_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт з 7.30 до 12.30, Сб-Нд з 8.30 до 13.00')

# @dp.message_handler(commands=['Місцезнаходження точок видачі'])
async def milk_factory_places_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'вул. Тракторобудівників, 18\
                                                  вул. Квітнева, 144А\
                                                  вул. Біблика, 74', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['Menu'])
async def milk_factory_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(milk_factory_open_command, commands=['Mode'])
    dp.register_message_handler(milk_factory_places_command, commands=['Place'])
    dp.register_message_handler(milk_factory_menu_command, commands=['Menu'])
