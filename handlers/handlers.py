from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from handlers.keyboards import kb_exchange
from utils import currency_exchange

router = Router()
@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Valyuta ayirboshlash botiga xush kelibsiz!", reply_markup=kb_exchange)


@router.message(F.text == "💲 ➡️ 🇺🇿")
async def enter_summa(msg: Message):
    await msg.answer("Summani kiriting: ")

@router.message(F.text)
async def usd_to_sum(msg: Message):
    summa = int(msg.text)
    kurs = await currency_exchange("USD", "UZS")
    await msg.answer(f"{summa} --> UZS = {summa * kurs} USZ")