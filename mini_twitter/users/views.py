from django.shortcuts import render
from .models import User
from posts.models import Post, Comment

def user_list(request): # список всех юзеров
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user/user_list.html', context)





