import io

import aiohttp
from aiogram import Router, types
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.utils.chat_action import ChatActionSender

router = Router(name=__name__)


@router.message(Command("code", prefix="/!%"))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        "Это язык программирования Python:",
        "",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "print('Hello world!')",
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
                "console.log('Hello world!')",
                "\n",
                "function foo() {\n  return 'bar'\n}",
                sep="\n",
            ),
            language="javascript",
        ),
        sep="\n",
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


@router.message(Command('pic'))
async def handle_command_pic_url(message: types.Message):
    url = 'https://stihi.ru/pics/2023/03/01/2507.jpg'
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.reply_photo(
        photo=url,
        caption='Кот породы Сфинкс'
    )


@router.message(Command('file'))
async def handle_command_pic_path(message: types.Message):
    file_path = r"C:\Users\Тимур\Downloads\sphynx.jpeg"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    await message.reply_document(
        document=types.FSInputFile(
            path=file_path,
        ),
        caption='Кот породы Сфинкс',
    )


@router.message(Command("text"))
async def send_txt_file(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    file = io.StringIO()
    file.write("Hello world!\n")
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="file.txt"
        ),
    )


async def sent_big_file(message: types.Message):
    file = io.BytesIO()
    url = "https://kotey-ka.ru/wp-content/uploads/2017/05/11111.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_bytes = await response.read()
    file.write(result_bytes)
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue(),
            filename="Кот сфинкс, большая картинка"
        ),
    )


@router.message(Command("pic_file"))
async def send_pic_file_buffered(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    async with ChatActionSender.upload_document(
            bot=message.bot,
            chat_id=message.chat.id,
    ):
        await sent_big_file(message)
