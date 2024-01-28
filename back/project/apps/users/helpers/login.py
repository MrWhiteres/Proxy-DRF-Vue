from dataclasses import dataclass

from project.apps.users.data import base
from project.apps.users.data.base import ForUser
from project.apps.users.helpers.sub import get_user


@dataclass
class Login(ForUser):
    email: str
    password: str

    form: base.LoginData = None

    def convert_data(self) -> base.LoginData:
        return base.LoginData(
            email=self.email,
            password=self.password
        )

    def get_user(self) -> None:
        self.user = get_user(email=self.email).user
