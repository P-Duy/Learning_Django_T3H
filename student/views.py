from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.db.models import Q

from .models import Student


# Create your views here.
def student_view(request):
    # kiem tra sort
    sort = request.GET.get("sort")
    if sort not in ["-created_at", "created_at"]:
        sort = "-created_at"
    # Phan trang
    page = request.GET.get("page")
    limit = request.GET.get("limit")
    if not limit or not limit.isnumeric():
        limit = settings.LIMIT_STUDENTS

    keyword = request.GET.get("keywordInput")

    if keyword:
        students = Student.objects.filter(
            Q(ho__contains=keyword) | Q(ten__contains=keyword)
        )
    else:
        students = Student.objects.all()

    # sort
    students = students.order_by(sort)

    students_paginator = Paginator(students, limit)
    try:
        students_paginator = students_paginator.page(page)
    except PageNotAnInteger:
        students_paginator = students_paginator.page(1)
    except EmptyPage:
        students_paginator = students_paginator.page(students_paginator.num_pages)

    context = {
        "students": students_paginator,
        "keywordInput": keyword if keyword else "",
    }
    return render(request, "student/student_views.html", context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {"student": student}
    return render(request, "student/student_detail.html", context)
