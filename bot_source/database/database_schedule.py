import sqlite3
from create_bot import bot, dp


def start_sqlite():
    global base, cur
    base = sqlite3.connect('bot_source/database/university_schedule.db')
    cur = base.cursor()
    if base:
        print('Database connected successfully')


async def db_read(state):
    async with state.proxy() as data:
        cur.execute("SELECT Schedule FROM UNIVERSITY WHERE Faculty=? AND Month=? AND Date=?", tuple(data.values()))
        result = cur.fetchone()
        str_result = ''.join(result).replace('%', '\n')
        return str_result

