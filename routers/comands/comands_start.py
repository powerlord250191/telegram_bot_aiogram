from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://telegrambot.biz/images/avatars/2457.png"
    await message.answer(
        text=f'{markdown.hide_link(url)}Привет {markdown.hbold(message.from_user.full_name)}! Что я могу для тебя сделать?',
        parse_mode=ParseMode.HTML,
    )


@router.message(Command("help", prefix="!/"))
async def handle_help(message: types.Message):
    text = markdown.text(
        markdown.markdown_decoration.quote("Я простой эхо бот."),
        markdown.text(
            "Отправь мне",
            markdown.markdown_decoration.bold(
                markdown.text(
                    markdown.underline("буквально"),
                    markdown.markdown_decoration.italic(
                        markdown.text(
                            "любое"
                        ),
                    ),
                ),
            ),
            markdown.markdown_decoration.quote("сообщение!"),
        ),
        sep="\n",
    )
    await message.answer(
        text=text, parse_mode=ParseMode.MARKDOWN_V2
    )
