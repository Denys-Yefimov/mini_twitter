from django.contrib import admin
from .models import Post, Comment

# Реєстрація моделей для відображення в адмінці
admin.site.register(Post)
admin.site.register(Comment)
