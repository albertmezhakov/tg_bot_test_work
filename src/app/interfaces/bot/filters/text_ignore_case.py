from aiogram.filters import BaseFilter
from aiogram.types import Message


class TextInIgnoreCase(BaseFilter):
    def __init__(self, triggers: list[str]):
        self.triggers = [t.lower() for t in triggers]

    async def __call__(self, message: Message) -> bool:
        return message.text and message.text.lower() in self.triggers
