from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup

from config import db
from utils.keyboards import request_contact_kb, request_location_kb
from utils.states import RegisterStates

reg_router = Router()

@reg_router.message(RegisterStates.first_name)
async def register_first_name(message: Message, state: FSMContext) -> None:
    await state.update_data(first_name=message.text)
    await state.set_state(RegisterStates.last_name)
    await message.answer("Iltimos, endi familiyangizni kiriting ...")

@reg_router.message(RegisterStates.last_name)
async def register_last_name(message: Message, state: FSMContext) -> None:
    await state.update_data(last_name=message.text)
    await state.set_state(RegisterStates.phone)
    await message.answer(
        "Iltimos, endi telefon raqamingizni yuboring ...",
        reply_markup=request_contact_kb
    )

@reg_router.message(RegisterStates.phone, F.contact)
async def register_phone(message: Message, state: FSMContext) -> None:
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(RegisterStates.address)
    await message.answer(
        "Iltimos, endi manzilingizni yozing yoki location yuboring ...",
        reply_markup=request_location_kb
    )

@reg_router.message(RegisterStates.phone)
async def register_phone_error(message: Message, state: FSMContext) -> None:
    await message.reply(
        "Iltimos, telefon raqamingizni yuboring ...",
        reply_markup=request_contact_kb
    )

@reg_router.message(RegisterStates.address)
async def register_address(message: Message, state: FSMContext) -> None:
    if dict(message)['location']:
        await state.update_data(location=dict(message.location))
    else:
        await state.update_data(address=message.text)

    info = await state.get_data()

    try:
        db.register_user(
            message.from_user.id,
            info["first_name"],
            info["last_name"],
            info.get("address", None),
            info.get("location", None),
            info["phone"]
        )
        await state.clear()
        await message.answer(
            f"Hurmatli {info['first_name']} {info['last_name']}, siz muvaffaqiyatli roýxatdan o'tdingiz!")
    except Exception as e:
        print(e)
        await message.answer("Roýxatdan o'tishda xatolik yuz berdi, iltimos, birozdan so'ng qayta urinib ko'ring!")
