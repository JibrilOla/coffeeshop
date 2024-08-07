from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Reservation

# Create your views here.


def Res(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            date = request.POST.get("date")
            time = request.POST.get("time")
            persons = request.POST.get("persons")

            reservation_s = Reservation.objects.create(
                user=request.user,
                name=name,
                email=email,
                date=date,
                time=time,
                persons=persons,
            )
            reservation_s.save()
            context = {"date": date, "time": time, "persons": persons}
            return render(request, "csapp/ssr.html", context)

        data = {"title": "Reservation"}
        return render(request, "csapp/reservation.html", data)
    else:
        return redirect("/login")

def ResDetails(request):
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(user=request.user).order_by("-date")
        return render(request, "csapp/rdetails.html", {"reservations":reservations})
    else:
        return redirect("/login")