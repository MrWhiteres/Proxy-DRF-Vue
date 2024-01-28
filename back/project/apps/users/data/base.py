from abc import ABC
from dataclasses import dataclass

from rest_framework_simplejwt.tokens import RefreshToken

from ..models import User


@dataclass
class GetUser:
    user: User = None
    success: bool = False
    error: dict = None


@dataclass
class LoginData:
    email: str
    password: str


@dataclass
class RegisterData:
    username: str
    email: str
    password: str
    password2: str


@dataclass
class UserData:
    username: str
    email: str


class ForUser(ABC):
    user: User = None

    def __post_init__(self):
        self.form = self.convert_data()

    def convert_data(self) -> dataclass:
        """
        Convert data from dataclass
        :param self:
        :return:
        """

    def create_token(self) -> dict:
        refresh = RefreshToken.for_user(self.user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
