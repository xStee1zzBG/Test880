import asyncio
import logging
import os
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен бота
TOKEN = os.getenv('6403585791:AAFX12CIj1Kg7NC3Z843_XjwyJ5wSRy8Spw')

# Инициализация бота и диспетчера
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы в базе данных, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
''')
conn.commit()

@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    # Проверка, есть ли уже пользователь в базе данных
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    if cursor.fetchone() is None:
        # Если пользователя нет, добавляем его
        cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
        conn.commit()
        await message.answer("Добро пожаловать! Вы зарегистрированы.")
    else:
        await message.answer("Вы уже зарегистрированы.")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
