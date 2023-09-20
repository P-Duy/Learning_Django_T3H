from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def login2(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        is_auth = authenticate(username=username, password=password)
        if is_auth:
            login(request, is_auth)
            return redirect("home:home")
        else:
            error = "username and password is incorrect"

    context = {
        "error": error,
    }
    return render(request, "login2/login.html", context)
