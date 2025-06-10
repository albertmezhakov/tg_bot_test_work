from aiogram import Bot, types


async def setup_bot_commands(bot: Bot) -> None:
    commands = [
        types.BotCommand(command="set_info", description="Добавить инфу о себе, чтобы все знали кто самый сильный игрок тут.")
    ]
    await bot.delete_my_commands()
    await bot.set_my_commands(commands)
