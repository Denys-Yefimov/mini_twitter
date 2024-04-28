from django.urls import path
from .views import UserListView, UserDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_posts'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


