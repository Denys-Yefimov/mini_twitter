from django.shortcuts import render
from .models import User
from django.views.generic import ListView


# def user_list(request): # список всех юзеров
#     users = User.objects.all()
#     context = {'users': users}
#     return render(request, 'user/user_list.html', context)


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'




