from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, Tag


def index_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by('-created_at').all()
    tags = Tag.objects.all()
    return render(request, "index.html", {
        'posts': posts,
        'tags': tags,
    })


def post_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    tags = Tag.objects.all()
    return render(request, "post.html", {
        'post': post,
        'tags': tags,
    })


def tag_view(request: HttpRequest, tag_name: str) -> HttpResponse:
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag).order_by('-created_at').all()
    tags = Tag.objects.all()
    return render(request, "index.html", {
        'posts': posts,
        'tags': tags,
    })
