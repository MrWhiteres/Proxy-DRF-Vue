from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken

from ..data import base
from ..models import User


def get_user(email: str, username: str = None) -> base.GetUser:
    if email and username:
        user = User.objects.filter(Q(email=email) | Q(username=username))
    else:
        user = User.objects.filter(email=email)
    if user.exists():
        return base.GetUser(user=user.first())
    return base.GetUser()


def logout(token: str) -> None:
    try:
        token = RefreshToken(token)
        token.blacklist()
    except Exception:
        pass
