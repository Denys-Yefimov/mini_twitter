from django.urls import path
from custom_auth.views import RegisterView, login_view

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name="register"),
    path('login/', login_view, name='login'),
]