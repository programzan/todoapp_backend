from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager

from core.enums import UserRoleEnum


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


class ActiveQuerySet(models.QuerySet):
    """Base QuerySet with filtering by is_active attr"""
    def active(self):
        return self.filter(is_active=True)


class UserManager(DjangoUserManager):
    def students(self):
        return self.filter(role=UserRoleEnum.STUDENT)


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRoleEnum.as_choices(),
        verbose_name='Роль',
        default=UserRoleEnum.STUDENT.value,
    )

    def is_student(self):
        return self.role == UserRoleEnum.STUDENT.value

    def is_teacher(self):
        return self.role == UserRoleEnum.TEACHER.value


class Project(models.Model):
    pass
