from enum import Enum


class UserRoleEnum(str, Enum):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'

    def __str__(self):
        return self.value

    @classmethod
    def as_choices(cls):
        return (
            (cls.STUDENT.value, 'Студент'),
            (cls.TEACHER.value, 'Преподаватель'),
        )
