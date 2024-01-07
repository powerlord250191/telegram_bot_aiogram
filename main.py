import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from config import API_KEY
from config import BOT_TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f'Привет {message.from_user.full_name}! Что я могу для тебя сделать?')


@dp.message(Command('help'))
async def handle_help(message: types.Message):
    # text = 'Я простой эхо бот!\nОтправь мне любое сообщение!'
    # entity_bold = types.MessageEntity(
    #     type="bold",
    #     offset=len('Я простой эхо бот!\nОтправь мне '),
    #     length=5)
    # entities = [entity_bold]
    text = markdown.text(
        'Я простой эхо бот\\.',
        markdown.text(
            'Отправь мне',
            markdown.bold('любое'),
            'сообщение\\!'),
        sep='\n'
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2
    )


@dp.message()
async def echo_message(message: types.Message):
    await message.answer(
        text='Подождите секунду пожалуйста'
    )
    # if message.text:
    #     await message.answer(
    #         text=message.text,
    #         entities=message.entities,
    #     )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Я не знаю что вам ответить, извините:(")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
