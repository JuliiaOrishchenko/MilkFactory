import sqlite3
import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('pizza_sushi.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, category TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(chat_id, category):
    cur.execute(f'SELECT * FROM menu WHERE category="{category}"')
    rets = cur.fetchall()
    for ret in rets:
        photo_url, name, description, price, category = ret
        caption = f'{ret[1]}\nОпис: {ret[2]}\nЦіна {ret[-1]}'
        await bot.send_photo(chat_id, photo_url, caption)

async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()

