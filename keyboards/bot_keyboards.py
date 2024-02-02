from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonText:
    HELLO = "Привет!"
    WHATS_NEXT = "Что дальше?"
    BYE = "До свидания"


def get_on_start_keyboard():
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WHATS_NEXT)
    button_bye = KeyboardButton(text=ButtonText.BYE)
    button_first_row = [button_hello, button_help]
    button_second_row = [button_bye]
    markup = ReplyKeyboardMarkup(
        keyboard=[button_first_row, button_second_row],
        resize_keyboard=True,
    )
    return markup
