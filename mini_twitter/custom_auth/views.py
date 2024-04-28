from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from custom_auth.forms import CustomUserCreateForm, LoginForm


class RegisterView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'custom_auth/register.html'


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post-list')
    else:
        form = LoginForm()
        return render(request, 'custom_auth/login.html', context={'form': form})
