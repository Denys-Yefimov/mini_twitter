from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from custom_auth.forms import CustomUserCreateForm, LoginForm
from custom_auth.models import CustomUser
from django.views.generic import ListView, DetailView
from posts.views import Post


class UserListView(ListView):
    model = CustomUser
    template_name = 'user/user_list.html'


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user/user_posts.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        posts = Post.objects.filter(user=user)
        context['posts'] = posts
        return context
