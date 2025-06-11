from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.interfaces.bot.features import features
from app.interfaces.bot.filters.text_ignore_case import TextInIgnoreCase
from app.interfaces.bot.keyboards import keyboards
from app.interfaces.bot.states.profile import ProfileState
from app.use_cases.user_profile_service import UserProfileService

router = Router()


@router.message(TextInIgnoreCase(features.set_info.triggers))
async def set_info_cmd(message: Message, state: FSMContext):
    await state.set_state(ProfileState.name)
    await message.answer("Напишите ваше имя", reply_markup=keyboards.cancel_kb.as_reply_markup())


@router.message(ProfileState.name, F.text)
async def handle_name(message: Message, state: FSMContext, user_profile_service: UserProfileService):
    name = message.text
    user_id = message.from_user.id

    await user_profile_service.update_name(user_id, name)

    await state.set_state(ProfileState.info)
    await message.answer(
        "Отлично, записал. Теперь немного расскажите о себе.", reply_markup=keyboards.cancel_kb.as_reply_markup()
    )


@router.message(ProfileState.info)
async def handle_info(message: Message, state: FSMContext, user_profile_service: UserProfileService):
    info = message.text
    user_id = message.from_user.id

    await user_profile_service.update_info(user_id, info)

    await state.set_state(ProfileState.photo)
    await message.answer(
        "Отлично, записал. Теперь скиньте свое фото.", reply_markup=keyboards.cancel_kb.as_reply_markup()
    )


@router.message(ProfileState.photo, F.photo)
async def handle_photo(message: Message, state: FSMContext, user_profile_service: UserProfileService):
    user_id = message.from_user.id
    photo = message.photo[-1]

    await user_profile_service.update_photo(user_id, photo.file_id)

    await state.clear()
    await message.answer("Готово, данные обновлены.", reply_markup=keyboards.menu_kb.as_reply_markup())


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
