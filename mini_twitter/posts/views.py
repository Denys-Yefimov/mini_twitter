from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from users.models import User
from django.views.generic import ListView
from posts.forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/posts_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context =super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'comment/comment_list.html'


def user_comment(request, username):    # комент конкретного пользователя
    user = User.objects.get(username=username)
    comment = Comment.objects.filter(user=user)
    context = {'user': user, 'comment': comment}
    return render(request, 'comment/user_comment.html', context)

# инфа по конкретному юзеру (username, email, profile_picture, посты конкретного юзера)
def user_posts(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'post/user_posts.html', context)


def add_post(request):  # добавление поста
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): # проходим валидацию
            print(form.cleaned_data)
            post = form.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})


def post_detail(request, post_id): # детали каждого поста
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects. filter(post=post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post/post_detail.html', context)


def add_comment(request, post_id):  # добавление комента к посту
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():  # проходим валидацию
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm(initial={'post': post})
    return render(request, 'post/create_comment_to_post.html', {'form': form, 'post': post})


class CommentsToPost(ListView):
    model = Post
    context_object_name = 'comments_to_post'
    template_name = 'post_comments.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context

    def get_queryset(self):
        posts = Post.objects.filter(post__id=self.kwargs['posts_id'])
        return posts