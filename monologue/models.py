from typing import Optional
import libgravatar
import markdown
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    permalink = models.CharField(max_length=128, blank=True)
    tags = models.ManyToManyField(Tag, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def render_content(self) -> str:
        return markdown.markdown(self.content, extensions=["tables", "toc"])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1024)
    name = models.CharField(max_length=64)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def gravatar_url(self, size: Optional[int] = 64) -> str:
        gravatar = libgravatar.Gravatar(self.email)
        return gravatar.get_image(size)
