from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

random_num_update_cb_data = "random_num_update_cb_data"


def build_actions_keyboard(random_number_button_text="Случайный номер") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=random_number_button_text,
        callback_data=random_num_update_cb_data,
    )
    return builder.as_markup()

