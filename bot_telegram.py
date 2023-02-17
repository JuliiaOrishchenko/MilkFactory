from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Bot is online')
    sqlite_db.sql_start()

from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

# @dp.message_handler()
# async def echo_send(message: types.Message):
#     # await message.answer(message.text)
#     await message.reply(message.text)
#     # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)