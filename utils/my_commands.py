from aiogram.types import BotCommand

custom_commands = [
    BotCommand(
        command="start",
        description="Bot qayta ishga tushirish",
    ),
    BotCommand(
        command="yordam",
        description="Botdan foydalanish qo'llanmasi",
    ),
    BotCommand(
        command="register",
        description="Botdan roýxatdan o'tish",
    ),
    BotCommand(
        command="set_avatar",
        description="Avatar qo'shish",
    ),
    BotCommand(
        command="my_avatar",
        description="Mening avatarimni ko'rish",
    )
]