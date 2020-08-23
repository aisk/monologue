from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404

from . import forms
from .models import Comment, Post, Tag


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
    comments = Comment.objects.filter(article=post).order_by('created_at').all()
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest(form.errors.as_ul())
        comment = form.save(commit=False)
        comment.article = post
        comment.save()
    return render(request, "post.html", {
        'post': post,
        'tags': tags,
        "comments": comments,
    })


def tag_view(request: HttpRequest, tag_name: str) -> HttpResponse:
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag).order_by('-created_at').all()
    tags = Tag.objects.all()
    return render(request, "index.html", {
        'posts': posts,
        'tags': tags,
    })
