from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def Register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            xval = form.save()
            print("*****", xval)
            return redirect("/login")
    data = {"ptitle": Register, "pslug": "- Register -", "form": form}
    return render(request, "register/register.html", data)


def Login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        userx = authenticate(request, username=user, password=password)
        if userx is not None:
            login(request, userx)
            return redirect("/home")
        else:
            return redirect("/login")

    data = {"pslug": "- Login -", "ptitle": "Login", "popp": "register"}
    return render(request, "register/login.html", data)


def Dashboard(request):
    if request.user.is_authenticated:
        return render(request, "csapp/dashboard.html")
    else:
        return redirect("/login")
