
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from custom_auth.models import CustomUser  # Импорт модели CustomUser из custom_auth
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.functional import SimpleLazyObject
from .models import Post, Comment
from .forms import PostForm, CommentForm






class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/posts_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = super().get_queryset()
        return query.select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all()
        return context


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'comment/comment_list.html'


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Используйте объект пользователя из custom_auth
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_queryset(self):
        query = super().get_queryset()
        return query.prefetch_related('comment_set')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comment_set.all()
        return context


class AddCommentView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'post/create_comment_to_post.html'

    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)

        # Получаем фактический объект пользователя
        user = self.request.user
        if isinstance(user, SimpleLazyObject):
            user = get_user_model().objects.get(pk=user.pk)

        form.instance.post = post
        form.instance.user = user  # Присваиваем текущего пользователя
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs['post_id']
        return context



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
