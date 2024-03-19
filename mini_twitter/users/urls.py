from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_posts'),
]


