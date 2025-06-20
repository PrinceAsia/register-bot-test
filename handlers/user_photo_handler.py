from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import db
from utils.states import AvatarStates

user_photo_router = Router()

@user_photo_router.message(Command('set_avatar'))
async def set_avatar_command_handler(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AvatarStates.user_avatar)
    await message.answer("Iltimos, PNG yoki JPG formatdagi rasmingizni yuboring...")

@user_photo_router.message(AvatarStates.user_avatar, F.photo)
async def set_user_avatar(message: Message, state: FSMContext):
    await state.clear()
    if db.set_avatar(message.from_user.id, message.photo[0].file_id):
        await message.answer("Avatar muvaffaqiyatli sozlandi!")
    else:
        await message.answer("Avatarni joylashda xatolik yuz berdi, iltimos, birozdan so'ng qayta urinib ko'ring!")

@user_photo_router.message(AvatarStates.user_avatar)
async def set_user_avatar_error(message: Message, state: FSMContext):
    await message.answer("Iltimos, rasm yuboring!")

@user_photo_router.message(Command('my_avatar'))
async def my_avatar(message: Message):
    avatar = db.get_avatar(message.from_user.id)
    if avatar:
        await message.answer_photo(
            photo=avatar,
            caption="Sizning avataringiz 👆👆👆",
        )
    else:
        await message.answer("Siz hali avatar joylamagansiz, joylash uchun /set_avatar buyrug'ini bosing!")
