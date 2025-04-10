import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from handlers.handlers import router as handlers_router
from handlers.commands import set_bot_menu
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(handlers_router)
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    await set_bot_menu(bot)


if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())
