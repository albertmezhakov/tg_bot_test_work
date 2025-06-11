from aiogram import Bot, types

from app.interfaces.bot.features.feature_entry import FeatureEntry


async def setup_bot_commands(bot: Bot) -> None:
    cmds: list[FeatureEntry] = FeatureEntry.commands_to_set
    bot_commands = [types.BotCommand(command=ftr.slashed_command, description=ftr.slashed_command_descr) for ftr in
                    cmds]
    await bot.delete_my_commands()
    await bot.set_my_commands(bot_commands)
