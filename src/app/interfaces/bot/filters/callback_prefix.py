from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class CallbackPrefixFilter(BaseFilter):
    def __init__(self, prefix: str):
        self.prefix = prefix

    async def __call__(self, query: CallbackQuery) -> bool:
        return query.data and query.data.split(":")[0] == self.prefix
