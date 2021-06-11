from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.TextField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    cover = models.FileField(upload_to='video/')
    body = models.TextField()

    def __str__(self):
        return self.title
