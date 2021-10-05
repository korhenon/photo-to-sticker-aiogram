from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
from converter import Converter
from utils import States

# Bot init

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Handlers

# Command handler
@dp.message_handler(commands=["sticker"])
async def set_wait_photo_state(message: types.Message):
    await message.answer("Send photo:")
    await States.WAIT_PHOTO_STATE.set() # Set state

@dp.message_handler(state=States.WAIT_PHOTO_STATE, content_types=["photo"])
async def convert_photo(message: types.Message, state: FSMContext):
    await message.photo[-1].download('input.png')
    Converter().convert() # Converting input image to sticker
    file = open('output.png', 'rb') # Opening output image
    await message.answer_document(file)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)
