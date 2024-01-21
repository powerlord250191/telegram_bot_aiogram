from aiogram import Router, F, types

router = Router(name=__name__)
any_media_filter = F.photo | F.video | F.document


@router.message(F.photo, ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    caption = "Я не вижу, извини. Можешь подписать эту картинку?"
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )


@router.message(any_media_filter, ~F.caption)
async def handle_any_media_wo_caption(message: types.Message):
    if message.document:
        await message.reply_document(
            message.document.file_id
        )
    elif message.video:
        await message.reply_video(
            video=message.video.file_id,
        )
    else:
        await message.reply("Я не вижу, извини. Не ругайся на меня.")


@router.message(F.photo, F.caption.contains("пожалуйста"))
async def handle_photo_with_please_caption(message: types.Message):
    await message.reply("Я не вижу, простите")


@router.message(any_media_filter, F.caption)
async def handle_any_media_w_caption(message: types.Message):
    await message.reply(f"Какой-то медиа файл. Ваш текст: {message.caption!r}")
