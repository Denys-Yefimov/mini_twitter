from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from users.models import User

from posts.forms import PostForm, CommentForm

def post_list(request): # просмотр всех постов
    posts = Post.objects.all()
    users = User.objects.all()
    context = {'posts': posts, 'users': users}
    return render(request, 'post/posts_list.html', context)

def comment_list(request): # просмотр всех коментов
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'comment/comment_list.html', context)


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


def post_comments(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comment_set.all()  # Получаем все комментарии для данного поста
    return render(request, 'post_comments.html', {'post': post, 'comments': comments})