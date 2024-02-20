from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonPollType,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonText:
    HELLO = "Привет!"
    WHATS_NEXT = "Что дальше?"
    BYE = "До свидания"


def get_on_start_keyboard() -> ReplyKeyboardMarkup:
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WHATS_NEXT)
    button_bye = KeyboardButton(text=ButtonText.BYE)
    button_first_row = [button_hello, button_help]
    button_second_row = [button_bye]
    markup = ReplyKeyboardMarkup(
        keyboard=[button_first_row, button_second_row],
        resize_keyboard=True,
        # one_time_keyboard=True,
    )
    return markup


def get_on_help_keyboard() -> ReplyKeyboardMarkup:
    numbers = [
        "1️⃣",
        "2️⃣",
        "3️⃣",
        "4️⃣",
        "5️⃣",
        "6️⃣",
        "7️⃣",
        "8️⃣",
        "9️⃣",
        "0️⃣"
    ]
    builder = ReplyKeyboardBuilder()
    for num in numbers:
        # builder.button(text=num)
        builder.add(KeyboardButton(text=num))
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=False)


def get_actions_kb() -> ReplyKeyboardMarkup:
    #     markup = ReplyKeyboardMarkup()
    #     return markup
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="🌎 Отправить локацию",
        request_location=True,
    ),
    builder.button(
        text="☎️ Отправить телефон",
        request_contact=True,
    ),
    builder.button(
        text="📊 Отправить опрос",
        request_poll=KeyboardButtonPollType(),
    )
    builder.button(
        text="🚀 Отправить квиз",
        request_poll=KeyboardButtonPollType(type="quiz"),
    )
    builder.button(
        text="🥣 Отправить голосование 'Что на ужин?'",
        request_poll=KeyboardButtonPollType(type="regular"),
    )
    builder.button(text=ButtonText.BYE)
    builder.adjust(1)
    return builder.as_markup(
        input_field_placeholder="Действия:",
        resize_keyboard=True,
    )
