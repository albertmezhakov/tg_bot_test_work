from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class User:
    social_id: int
    id: Optional[int] = None
    username: Optional[str] = None
    registration_date: Optional[datetime] = None
    taps: int = 0
    name: Optional[str] = None
    info: Optional[str] = None
    photo: Optional[str] = None