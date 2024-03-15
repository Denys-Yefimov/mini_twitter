from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True, verbose_name='Email адреса')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата реєстрації')
    date_of_birth = models.DateTimeField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='books/profile_images', null=True, blank=True)

    def __str__(self):
        return f"{self.username}"


