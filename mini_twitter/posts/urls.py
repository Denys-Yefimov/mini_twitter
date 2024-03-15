from django.urls import path
from .views import post_list, comment_list, user_comment, user_posts, add_post, post_detail, add_comment, post_comments


urlpatterns = [
    path('', post_list, name='post-list'),
    path('comment', comment_list, name='comment-list'),
    path('comment/<str:username>/', user_comment, name='user-comment'),
    path('add-post/', add_post, name='add_post'),
    path('add-comment/<int:post_id>/', add_comment, name='add_comment'),
    path('user/<str:username>/', user_posts, name='user_posts'),
    path('post-detail/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/comments/', post_comments, name='post_comments'),
]

