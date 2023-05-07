# Generated by Django 4.2 on 2023-05-07 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedtask',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_user_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
