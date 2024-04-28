import random
from datetime import datetime
from django.core.management.base import BaseCommand
from posts.models import Post
from custom_auth.models import CustomUser


class Command(BaseCommand):
    help = "Fill DB with default data"

    def handle(self, *args, **options):
        # Создаем пользователей
        users = []
        for i in range(1, 3):
            user = CustomUser.objects.create(
                username=f"username {i}",
                email=f"user{i}@gmail.com",
                date_of_birth=datetime(year=2000 - random.randint(1, 30), month=1, day=1 + i)
            )
            users.append(user)

        # Создаем записи
        for i in range(90):
            Post.objects.create(
                title=f"Book {i}",
                user=random.choice(users),
            )

        self.stdout.write(self.style.SUCCESS('DB successfully filled'))
