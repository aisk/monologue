from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def index_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("It works!")


def post_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {
        'post': post,
    })
