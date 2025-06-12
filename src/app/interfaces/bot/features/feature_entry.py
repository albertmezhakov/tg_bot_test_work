from __future__ import annotations

from typing import ClassVar


class FeatureEntry:
    commands_to_set: ClassVar[list[FeatureEntry]] = []

    def __init__(
        self,
        *,
        slashed_command: str | None = None,
        slashed_command_descr: str | None = None,
        button: str | None = None,
        commands: list[str] | None = None,
        callback_action: str | None = None,
        set_to_bot_commands: bool = False,
    ):
        self.slashed_command = slashed_command
        self.slashed_command_descr = slashed_command_descr
        self.button = button
        self.commands = commands
        self.callback_action = callback_action

        if set_to_bot_commands:
            if not (self.slashed_command and self.slashed_command_descr):
                raise AttributeError("`slashed_command` and `slashed_command_descr` fields must be set")
            self.commands_to_set.append(self)

    @property
    def triggers(self) -> list[str]:
        _triggers = []
        if self.slashed_command:
            _triggers.append(self.slashed_command)
        if self.button:
            _triggers.append(self.button.lower())
        if self.commands:
            _triggers.extend(self.commands)
            for com in self.commands:
                _triggers.append(com.capitalize())
        return _triggers
