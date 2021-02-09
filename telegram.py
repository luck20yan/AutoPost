import asyncio
import config
from aiogram import Bot, types

bot = Bot(token=config.telegram_token)


async def send_post_text(text):
    await bot.send_message(config.telegram_channel, text)


async def send_post_with_images(text, image):
    await bot.send_photo(config.telegram_channel, photo=open(image, 'rb'), caption=text)


async def send_post_images(images):
    media = types.MediaGroup()
    for image in images:
        media.attach_photo(types.InputFile(image), 'photo')
    await bot.send_media_group(config.telegram_channel, media=media)


async def send_post_a(text, images):
    if len(images) == 0:
        await send_post_text(text)
    elif len(images) == 1:
        await send_post_with_images(text, images[0])
    else:
        await send_post_text(text)
        await send_post_images(images)


def send_post(text, images):
    asyncio.run(send_post_a(text, images))
