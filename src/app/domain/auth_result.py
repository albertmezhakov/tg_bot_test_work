from dataclasses import dataclass
from enum import Enum


class AuthStatus(Enum):
    SUCCESS = "success"
    REGISTERED = "registered"
    NEED_PASSPHRASE = "need_passphrase"
    NEED_USERNAME = "need_username"


@dataclass
class AuthResult:
    status: AuthStatus
    message: str | None = None
