from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


random_site_cb_data = "random_site_cb_data"


def build_info_keyboard() -> InlineKeyboardMarkup:
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
    btn_random_site = InlineKeyboardButton(
        text="random_site",
        callback_data=random_site_cb_data,
    )
    row_tg = [tg_channel_btn, tg_chat_btn]
    # row_first = [tg_channel_btn]
    # row_second = [tg_chat_btn]
    rows = [
        # row_first,
        # row_second,
        row_tg,
        [bot_source_code_btn],
        [btn_random_site],

    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
