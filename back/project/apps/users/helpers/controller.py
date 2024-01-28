from project.abc_utils import data
from .login import Login
from .registration import Registration


def registration(user_data: data.Result) -> data.Result:
    worker = Registration(
        **user_data.data
    )
    worker.create_user()

    return data.Result(
        success=True,
        data=worker.create_token()
    )


def login(user_data: data.Result) -> data.Result:
    worker = Login(
        **user_data.data
    )
    worker.get_user()

    return data.Result(
        success=True,
        data=worker.create_token()
    )
