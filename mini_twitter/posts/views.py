from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Post, Comment
from users.models import User
from django.views.generic import ListView, DetailView, CreateView
from posts.forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/posts_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'comment/comment_list.html'


class AddPostView(CreateView):
    form_class = PostForm
    template_name = 'post/create_post.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        context['comments'] = comments
        return context


class AddCommentView(CreateView):
    form_class = CommentForm
    template_name = 'post/create_comment_to_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs['post_id']
        return context

    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        form.instance.post = post
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse_lazy('post_detail', kwargs={'pk': post_id})


class CommentsToPost(ListView):
    model = Comment
    context_object_name = 'comments_to_post'
    template_name = 'post_comments.html'

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs['post_id']
        return context
