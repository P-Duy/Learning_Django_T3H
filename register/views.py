from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home:home")

    context = {
        "form": form,
    }
    return render(request, "register/register.html", context)
