from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6403585791:AAFX12CIj1Kg7NC3Z843_XjwyJ5wSRy8Spw'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я твой бот на aiogram.")

# Обработчик эхо-сообщений
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
