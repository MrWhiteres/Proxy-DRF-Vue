from django.db import models

from project.abc_utils.models import AbcModels
from project.apps.users.models import User


class Site(AbcModels, models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    site = models.URLField(max_length=20000, )
