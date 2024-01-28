from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from project.abc_utils.models import AbcModels


class User(AbcModels, AbstractUser):
    username = models.CharField(_("username"), max_length=20, unique=True, db_index=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = 'Лист профілів'
