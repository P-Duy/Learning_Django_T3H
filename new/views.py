from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from .models import NewsModel


# Create your views here.
def new_view(request):
    page = request.POST.get("page")
    limit = request.GET.get("limit")
    if not limit or not limit.isnumeric():
        limit = settings.LIMIT_DEFAULT

    keyword = request.GET.get("keywordInput")
    if keyword:
        news = (
            NewsModel.objects.filter(title__contains=keyword)
            .values()
            .order_by("created_at")
        )
    else:
        news = NewsModel.objects.all().order_by("-created_at")
    news_paginator = Paginator(news, limit)
    try:
        news_paginator = news_paginator.page(page)
    except PageNotAnInteger:
        news_paginator = news_paginator.page(1)
    except EmptyPage:
        news_paginator = news_paginator.page(news_paginator.num_pages)
    context = {
        "news": news_paginator,
        "keywordInput": keyword if keyword else "",
    }
    return render(request, "new/new.html", context)


def new_post(request, pk):
    # news = NewsModel.objects.filter(pk=pk).values()[0]
    # context = news

    news = get_object_or_404(NewsModel, pk=pk)
    context = {"news": news}
    return render(request, "new/new_post.html", context)
