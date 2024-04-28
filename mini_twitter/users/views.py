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

class RegisterView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post-list')
    else:
        form = LoginForm()
        return render(request, 'user/login.html', context={'form': form})
