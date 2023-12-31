import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.filters import Command
import config

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f'Привет {message.from_user.full_name}! Что я могу для тебя сделать?')


@dp.message(Command('help'))
async def handle_help(message: types.Message):
    text = 'Я простой эхо бот!\nОтправь мне любое сообщение!'
    await message.answer(text=text)


@dp.message()
async def echo_message(message: types.Message):
    await message.answer(
        text='Подождите секунду пожалуйста'
    )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Я не знаю что вам ответить, извините:(")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
