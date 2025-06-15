from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from app.domain.user import User
from app.interfaces.api.dependencies import get_profile_service
from app.use_cases.user_profile_service import UserProfileService

router = APIRouter(prefix="/profile", tags=["profile"])


class ProfileOut(BaseModel):
    id: int
    username: str
    taps: int


class ProfileUpdateName(BaseModel):
    name: Optional[str] = None


@router.get("/{user_id}", response_model=ProfileOut)
async def get_profile(
    user_id: int, user_profile_service: Annotated[UserProfileService, Depends(get_profile_service)]
) -> ProfileOut:
    profile: User = await user_profile_service.get_user(user_id)
    if profile is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return ProfileOut(id=profile.id, username=profile.username, taps=profile.taps)


@router.post("/{user_id}/name", response_model=ProfileOut)
async def update_profile_name(
    user_id: int,
    payload: ProfileUpdateName,
    user_profile_service: Annotated[UserProfileService, Depends(get_profile_service)],
) -> ProfileOut:
    profile: User = await user_profile_service.update_name(user_id, name=payload.name)
    if profile is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return ProfileOut(id=profile.id, username=profile.username, taps=profile.taps)
