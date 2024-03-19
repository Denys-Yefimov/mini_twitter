from django.urls import path
from .views import (PostListView, CommentListView,
                    AddPostView, PostDetailView, AddCommentView, CommentsToPost)


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('comment', CommentListView.as_view(), name='comment-list'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('add-comment/<int:post_id>/', AddCommentView.as_view(), name='add_comment'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/comments/', CommentsToPost.as_view(), name='post_comments'),
]

