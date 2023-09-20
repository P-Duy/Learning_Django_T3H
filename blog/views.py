from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from .models import PostModel
from .forms import PostForm, PostModelForm


# Create your views here.
def blog(request):
    page = request.GET.get("page")

    # kiem tra sort
    sort = request.GET.get("sort")
    if sort not in ["-created_at", "created_at", "title"]:
        sort = "-created_at"

    # kiem tra gio han bai post
    limit = request.GET.get("limit")
    if not limit or not limit.isnumeric():
        limit = settings.LIMIT_DEFAULT

    keyword = request.GET.get("keywordInput")

    if keyword:
        posts = PostModel.objects.filter(title__contains=keyword).values()
    else:
        posts = PostModel.objects.all()

    # sort
    posts = posts.order_by(sort)

    post_paginator = Paginator(posts, limit)
    try:
        post_paginator = post_paginator.page(page)
    except PageNotAnInteger:
        post_paginator = post_paginator.page(1)
    except EmptyPage:
        post_paginator = post_paginator.page(post_paginator.num_pages)

    context = {
        "posts": post_paginator,
        "keywordInput": keyword if keyword else "",
    }
    return render(request, "blog/blog.html", context)


def post(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    context = {"post": post}
    return render(request, "blog/post.html", context)


def post_add(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render("blog/blog")

    context = {
        "form": form,
    }
    return render(request, "blog/post_add.html", context)


def post_edit(request, pk):
    model = PostModel.objects.get(pk=pk)

    form = PostModelForm(instance=model)

    if request.method == "POST":
        form = PostModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect("blog:post", model.id)

    context = {
        "form": form,
    }
    return render(request, "blog/post_edit.html", context)


def post_delete(request, pk):
    model = PostModel.objects.get(pk=pk)
    model.delete()
    return redirect("blog:blog")
