from django.shortcuts import render, get_object_or_404
from .models import User
from django.views.generic import ListView, DetailView
from posts.views import Post


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'

# инфа по конкретному юзеру (username, email, profile_picture, посты конкретного юзера)

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_posts.html'
    context_object_name = 'user'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        posts = Post.objects.filter(user=user)
        context['posts'] = posts
        return context

