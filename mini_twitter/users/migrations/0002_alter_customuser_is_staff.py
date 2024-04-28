from django.db import migrations
from users.models import CustomUser as CustomUserFromAuth


def copy_custom_users(apps, schema_editor):
    for user in CustomUserFromAuth.objects.all():
        CustomUser.objects.create(
            email=user.email,
            username=user.username,
            date_joined=user.date_joined,
            date_of_birth=user.date_of_birth,
            profile_picture=user.profile_picture,
            is_active=user.is_active,
            is_staff=user.is_staff
        )

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),  # Зависимость от вашей первоначальной миграции пользователей
    ]

    operations = [
        migrations.RunPython(copy_custom_users),  # Запускаем функцию для копирования пользователей
    ]
