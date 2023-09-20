from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from blog.models import PostModel
from new.models import NewsModel


# Create your views here.
def home(request):
    page = request.POST.get("page")
    limit_posts = settings.LIMIT_DEFAULT_MAX_HOME
    limit_news = settings.LIMIT_DEFAULT_MIN_HOME

    news = NewsModel.objects.all().order_by("-created_at")
    posts = PostModel.objects.all().order_by("-created_at")

    # hiển thị số bài niew
    news_paginator = Paginator(news, limit_news)
    try:
        news_paginator = news_paginator.page(page)
    except PageNotAnInteger:
        news_paginator = news_paginator.page(1)
    except EmptyPage:
        news_paginator = news_paginator.page(news_paginator.num_pages)

    # hiện thị số bài posts
    posts_paginator = Paginator(posts, limit_posts)
    try:
        posts_paginator = posts_paginator.page(page)
    except PageNotAnInteger:
        posts_paginator = posts_paginator.page(1)
    except EmptyPage:
        posts_paginator = posts_paginator.page(posts_paginator.num_pages)

    context = {
        "news_paginator": news_paginator,
        "posts_paginator": posts_paginator,
    }
    return render(request, "home/home.html", context)
