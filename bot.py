from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я помогу тебе учить слова. Добавь новое слово: /add")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
