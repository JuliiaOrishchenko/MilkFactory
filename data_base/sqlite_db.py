import sqlite3 as sq
from create_bot import bot
from keyboards import client_kb


def sql_start():
    global base, cur
    base = sq.connect('pizza_sushi.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, category TEXT, price TEXT)')
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
        await bot.send_photo(chat_id, photo_url, caption, reply_markup=client_kb.buy)


async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()


async def get_products(category):
    with sq.connect('pizza_sushi.db'):
        return cur.execute(f'SELECT * FROM menu WHERE category="{category}"').fetchall()


async def get_cart(user_id):
    con = sq.connect('pizza_sushi.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM cart WHERE user_id=(?)', (user_id,))
    cart_items = cur.fetchall()
    cur.close()
    con.close()
    return cart_items


async def add_to_cart(user_id, product_name, price):
    print(user_id, product_name)
    con = sq.connect('pizza_sushi.db')
    cur = con.cursor()
    print(f"Adding to cart: user_id={user_id}, product_name={product_name}, price={price}")
    cur.execute('INSERT INTO cart (user_id, product_name, price) VALUES(?, ?, ?)', (user_id, product_name, price))
    con.commit()
    cur.close()
    con.close()


async def cart_get_sum():
    con = sq.connect('pizza_sushi.db')
    cur = con.cursor()
    cur.execute("SELECT SUM(CAST(REPLACE(price, 'грн', '') AS DECIMAL(10, 2))) FROM cart")
    sum = cur.fetchone()[0]
    sum_str = str(sum)
    cur.close()
    con.close()
    return sum_str


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()
