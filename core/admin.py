from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            'Контакты',
            {
                'fields': (
                    'email',
                ),
            },
        ),
        (
            'Прочее',
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )
    list_filter = (
        'role',
        *UserAdmin.list_filter,
    )
    list_display = (
        'id',
        *UserAdmin.list_display,
        'role',
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return super().get_fieldsets(request, obj)
        fieldsets = super().fieldsets
        fieldsets[1][1]['fields'] = (
            'first_name',
            'last_name',
            'middle_name',
        )
        fieldsets += self.fieldsets
        return fieldsets
