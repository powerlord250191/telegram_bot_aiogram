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
    url = "https://telegrambot.biz/images/avatars/2457.png"
    await message.answer(text=f'{markdown.hide_link(url)}Привет {markdown.hbold(message.from_user.full_name)}! Что я могу для тебя сделать?',
                         parse_mode=ParseMode.HTML)


@dp.message(Command('help'))
async def handle_help(message: types.Message):
    # text = 'Я простой эхо бот!\nОтправь мне любое сообщение!'
    # entity_bold = types.MessageEntity(
    #     type="bold",
    #     offset=len('Я простой эхо бот!\nОтправь мне '),
    #     length=5)
    # entities = [entity_bold]
    text = markdown.text(markdown.markdown_decoration.quote(
        'Я простой эхо бот.'),
        markdown.text(
            'Отправь мне',
            markdown.markdown_decoration.bold(
                markdown.text(
                    markdown.underline('буквально'),
                    'любое',
                ),
            ),
            markdown.markdown_decoration.quote('сообщение!'),
        ),
        sep='\n'
    )
    await message.answer(
        text=text,
        parse_mode=None
        # parse_mode=ParseMode.MARKDOWN_V2
    )
@dp.message(Command("code"))
async def handle_comand_code(message: types.Message):
    text = markdown.text("Это язык программирования Python:",
                         "",
                         markdown.markdown_decoration.pre_language(
                             markdown.text(
                                 "print('Hello World!')",
                                 "\n",
                                 "def foo():\n    return 'bar'",
                                 sep="\n",
                             ),
                             language="python",
                         ),
                         "А это JS:",
                         "",
                         markdown.markdown_decoration.pre_language(
                             markdown.text(
                                 "console.log('Hello World!)",
                                 "\n",
                                 "function foo() {\n  return 'bar'\n}",
                                 sep="\n"
                             ),
                             language="javascript",
                         ),
                         sep="\n"
                         )
    await message.answer(text=text)

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(
        text='Подождите секунду, пожалуйста',
        parse_mode=None
    )
    # if message.text:
    #     await message.answer(
    #         text=message.text,
    #         entities=message.entities,
    #     )
    try:
        await message.copy_to(chat_id=message.chat.id)
        # await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Я не знаю что вам ответить, извините:(")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN,
              parse_mode=ParseMode.MARKDOWN_V2)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
