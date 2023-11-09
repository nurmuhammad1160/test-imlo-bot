import logging

from aiogram import Bot, Dispatcher, executor, types
from checkWord import checkWord
from transliterate import to_cyrillic, to_latin
API_TOKEN = '6735566082:AAHzURDVKe3UTvRujICOO2H1wdV3F-Z5GaU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("test imlo Botiga Xush Kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring.")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    to_latin(word)
    result = checkWord(word)
    # result = to_latin(result)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
            
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)