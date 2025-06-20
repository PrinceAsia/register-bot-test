import traceback

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import db
from utils.states import RegisterStates

basic_router = Router()

@basic_router.message(CommandStart())
async def cmd_start_handler(message: Message):
    if db.has_user(message.from_user.id):
        await message.reply(f"Qaytganingizdan xursandmiz!")
    else:
        try:
            db.add_user(dict(message.from_user))
        except Exception as e:
            print(e)
        await message.answer("Xush kelibsiz!")

@basic_router.message(Command('register'))
async def cmd_register_handler(message: Message, state: FSMContext):
    if db.is_registered(message.from_user.id):
        await message.reply(f"Siz botda avval roýxatdan o'tgansiz!")
    else:
        await state.clear()
        await state.set_state(RegisterStates.first_name)
        await message.reply(f"Roýxatdan o'tish jarayonini boshlaymiz\n"
                            f"Iltimos, ismingizni kiriting ...")

@basic_router.message()
async def all_message_handler(message: Message):
    await message.send_copy(message.from_user.id)