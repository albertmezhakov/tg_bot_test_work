from app.interfaces.bot.features.feature_entry import FeatureEntry

empty = FeatureEntry()

set_info = FeatureEntry(
    slashed_command="/set_info",
    slashed_command_descr="set profile info",
    button="Мой профиль",
    set_to_bot_commands=True,
)

ping_pong = FeatureEntry(
    commands=["ping", "health", "healthcheck"]
)

creator = FeatureEntry(
    commands=["creator"]
)

help_cmd = FeatureEntry(
    commands=["help"]
)
cancel = FeatureEntry(
    commands=["cancel"],
    button="Отмена",
    callback_action="cancel"
)

rating = FeatureEntry(
    slashed_command="/rating",
    slashed_command_descr="global rating",
    button="Рейтинг",
    set_to_bot_commands=True,
)

send_tap = FeatureEntry(
    slashed_command="/push_the_button",
    slashed_command_descr="we gonna push the button",
    button="Отправить кнопку",
    set_to_bot_commands=True,
)

tap_btn = FeatureEntry(
    button="Нажми на меня",
    callback_action="tap"
)

start = FeatureEntry(
    slashed_command="/start",
    slashed_command_descr="main menu",
    commands=["menu"],
    set_to_bot_commands=True
)
