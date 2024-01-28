from django.db import models


class AbcModels(models.Model):
    class Meta:
        abstract = True

    def return_data_self(self) -> str:
        return f'{self} - {self.__dict__}'

