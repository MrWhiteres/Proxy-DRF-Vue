from django.db import models

from project.abc_utils.models import AbcModels
from project.apps.users.models import User


class Site(AbcModels, models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    site = models.URLField(max_length=20000)
    traffic = models.FloatField(default=0)
    transition = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
