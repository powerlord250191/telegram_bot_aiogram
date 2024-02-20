from random import randint
from aiogram import F, Router
from aiogram.types import CallbackQuery
from keyboards.inline_keyboards.info_kb import (
    random_num_dice_cd_data,
    random_num_modal_cd_data,
)

router = Router(name=__name__)


@router.callback_query(F.data == random_num_dice_cd_data)
async def random_num_dice_cd(callback_query: CallbackQuery):
    await callback_query.answer(
        text=f"Твоё случайное число: {randint(1, 21)}",
        cache_time=5,
    )


@router.callback_query(F.data == random_num_modal_cd_data)
async def random_num_modal_cd(callback_query: CallbackQuery):
    await callback_query.answer(
        text=f"Cлучайное число: {randint(1, 100)}",
        cache_time=5,
        show_alert=True,
    )
