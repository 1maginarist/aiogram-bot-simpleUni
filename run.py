'''
   Start Bot
'''

from aiogram import executor
from create_bot import dp
from bot_source.handlers import client
from bot_source.database import database_schedule


async def on_startup(_):
    print('Bot is online')
    database_schedule.start_sqlite()

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




