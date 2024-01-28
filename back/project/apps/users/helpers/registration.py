from dataclasses import dataclass

from ..data import base
from ..data.base import ForUser
from ..models import User


@dataclass
class Registration(ForUser):
    username: str
    email: str
    password: str
    password2: str

    form: base.RegisterData = None

    def convert_data(self) -> base.RegisterData:
        return base.RegisterData(
            username=self.username,
            email=self.email,
            password=self.password,
            password2=self.password2
        )

    def create_user(self) -> None:
        self.user = User.objects.create_user(
            username=self.form.username,
            email=self.form.email,
            password=self.form.password
        )
