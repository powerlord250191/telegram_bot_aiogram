from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.bot_keyboards import (
    ButtonText,
    get_on_start_keyboard,
    get_actions_kb,
    get_on_help_keyboard,
)
from keyboards.bot_keyboards import get_on_help_keyboard
router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://telegrambot.biz/images/avatars/2457.png"
    await message.answer(
        text=f'{markdown.hide_link(url)}Привет {markdown.hbold(message.from_user.full_name)}! Что я могу для тебя сделать?',
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_keyboard(),
    )

@router.message(F.text == ButtonText.WHATS_NEXT)
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
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=get_on_help_keyboard(),
    )

@router.message(Command("more", prefix="!/more"))
async def handle_more(message: types.Message):
    markup = get_actions_kb()
    await message.answer(
        text="Выберите действие",
        reply_markup=markup
    )

@router.message(Command("info", prefix="!/"))
async def handle_info_comand(message: types.Message):
    tg_channel_btn = InlineKeyboardButton(
        text="📢 Канал",
        url="https://t.me/deni_mani"
    )
    tg_chat_btn = InlineKeyboardButton(
        text="💬 Чат",
        url="https://t.me/SurenTalk",
    )
    bot_source_code_btn = InlineKeyboardButton(
        text="🤖 исходный код этого бота",
        url="https://gitlab.skillbox.ru/timur_bolgov/python_basic_diploma/-/tree/step_1"
    )
    row_tg = [tg_channel_btn, tg_chat_btn]
    # row_first = [tg_channel_btn]
    # row_second = [tg_chat_btn]
    rows = [
        # row_first,
        # row_second,
        row_tg,
        [bot_source_code_btn],

    ]
    murkup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Ссылки и прочие ресурсы:",
        reply_markup=murkup,
    )
