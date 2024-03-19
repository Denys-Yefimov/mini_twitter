from django.db import models
from users.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.user}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})





class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:50]}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})



