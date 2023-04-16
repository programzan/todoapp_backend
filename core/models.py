from django.db import models
from django.contrib.auth.models import AbstractUser


class DefaultDateFieldsAbstractClass(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения',
    )

    class Meta:
        abstract = True


class DefaultFieldsManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)


class DefaultFieldsAbstractClass(DefaultDateFieldsAbstractClass):
    objects = DefaultFieldsManager()
    is_active = models.BooleanField(default=True, verbose_name='Активно?')

    class Meta:
        abstract = True


class User(AbstractUser):
    pass
