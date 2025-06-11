from app.interfaces.bot.features.feature_entry import FeatureEntry

empty = FeatureEntry()

set_info = FeatureEntry(
    slashed_command="/set_info",
    slashed_command_descr="set profile info",
    button="Мой профиль",
    set_to_bot_commands=True
)

ping_pong = FeatureEntry(
    commands=["ping", "health", "healthcheck"]
)

creator = FeatureEntry(
    commands=["creator"]
)

help = FeatureEntry(
    commands=["help"]
)
cancel = FeatureEntry(
    commands=["cancel"],
    callback_action="cancel"
)
