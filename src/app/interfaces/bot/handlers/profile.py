from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from app.interfaces.bot.states import ProfileState
from app.use_cases.user_profile_service import UserProfileService

router = Router()


@router.message(Command("set_info"))
async def set_info_cmd(message: Message, state: FSMContext):
    await state.set_state(ProfileState.name)
    await message.answer("Напишите ваше имя")


@router.message(ProfileState.name, F.text)
async def handle_name(message: Message, state: FSMContext, user_profile_service: UserProfileService):
    name = message.text
    user_id = message.from_user.id

    await user_profile_service.update_name(user_id, name)

    await state.set_state(ProfileState.info)
    await message.answer("Отлично, записал. Теперь немного расскажите о себе.")


@router.message(ProfileState.info)
async def handle_info(message: Message, state: FSMContext, user_profile_service: UserProfileService):
    info = message.text
    user_id = message.from_user.id

    await user_profile_service.update_info(user_id, info)

    await state.set_state(ProfileState.photo)
    await message.answer("Отлично, записал. Теперь скиньте свое фото.")


@router.message(ProfileState.photo, F.photo)
async def handle_photo(message: Message, state: FSMContext, user_profile_service: UserProfileService):
    user_id = message.from_user.id
    photo = message.photo[0]

    file = await message.bot.get_file(photo.file_id)
    file_path = file.file_path

    await user_profile_service.update_photo(user_id, file_path)

    await state.clear()
    await message.answer("Готово, данные обновлены.", reply_markup=_menu_kb())


def _menu_kb():
    # TODO: Вынести в keyboards.common
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню", callback_data="main_menu")
    return kb.as_markup()


@router.message(ProfileState.name)
async def handle_name_wrong_type(message: Message):
    # TODO: Вынести в texts.profile
    await message.answer("Не вижу в сообщении текста, попробуйте еще раз!")


@router.message(ProfileState.info)
async def handle_info_wrong_type(message: Message):
    # TODO: Вынести в texts.profile
    await message.answer("Не вижу в сообщении текста, попробуйте еще раз!")


@router.message(ProfileState.photo)
async def handle_photo_wrong_type(message: Message):
    # TODO: Вынести в texts.profile
    await message.answer("Не вижу в сообщении фото, попробуйте еще раз! Возможно вам нужно отправить фото без сжатия.")
