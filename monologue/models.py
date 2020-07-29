import markdown
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    permalink = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def render_content(self):
        return markdown.markdown(self.content, extensions=["tables"])

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1024)
    name = models.CharField(max_length=64)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
