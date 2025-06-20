from aiogram.fsm.state import StatesGroup, State


class RegisterStates(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    address = State()

class AvatarStates(StatesGroup):
    user_avatar = State()