from random import randint
from aiogram import F, Router
from aiogram.types import CallbackQuery
from keyboards.inline_keyboards.info_kb import random_site_cb_data

router = Router(name=__name__)

@router.callback_query(F.data == random_site_cb_data)
async def handle_random_site_cb(callback_query: CallbackQuery):
    bot_me = await callback_query.bot.me()
    await callback_query.answer(
        url=f"t.me/{bot_me.username}?start={randint(1, 100)}",
    )