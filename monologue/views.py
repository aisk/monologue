from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

from .models import Post


def index_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("It works!")


def post_view(request: HttpRequest, post_id: int) -> HttpResponse:
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404()
    return render(request, "post.html")