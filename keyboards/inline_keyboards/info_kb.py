from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .actions_kb import random_num_update_cb_data

random_num_dice_cd_data = "random_num_dice_cd_data"
random_num_modal_cd_data = "random_num_modal_cd_data"


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
        text="Сгенерировать случайное число от 1 до 100",
        callback_data=random_num_update_cb_data,
    )
    btn_random_num = InlineKeyboardButton(
        text="🎲 Случайное число",
        callback_data=random_num_dice_cd_data,
    )
    btn_random_num_modal = InlineKeyboardButton(
        text="👾 Случайное число",
        callback_data=random_num_modal_cd_data,
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
        [btn_random_num],
        [btn_random_num_modal],

    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
