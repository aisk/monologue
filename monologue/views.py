from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def index_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by('-created_at').all()
    return render(request, "index.html", {
        'posts': posts,
    })


def post_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {
        'post': post,
    })
