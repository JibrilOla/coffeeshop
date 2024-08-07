from django.shortcuts import render, redirect
from payments.models import UserWallet


# Create your views here.
def Home(request):
    return render(request, "csapp/home.html")


def About(request):
    data = {"title": "About"}
    return render(request, "csapp/about.html", data)


def Service(request):
    data = {"title": "Service"}
    return render(request, "csapp/service.html", data)


def Menu(request):
    if request.user.is_authenticated:
        data = {"title": "Menu"}
        return render(request, "csapp/menu.html", data)
    else:
        return redirect("/login")





def Contact(request):
    data = {"title": "Contact"}
    return render(request, "csapp/contact.html", data)


def Testimonial(request):
    data = {"title": "Testimonial"}
    return render(request, "csapp/testimonial.html", data)


def Dashboard(request):
    if request.user.is_authenticated:
        user_wallet = UserWallet.objects.get(user=request.user)
        data = {
            "balance": user_wallet.balance,
        }
        return render(request, "csapp/dashboard.html", data)
    else:
        return redirect("/login")
