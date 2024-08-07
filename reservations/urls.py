from django.urls import path
from .views import *

app_name = "reservations"
urlpatterns = [
    path("reservation/", Res, name="reservation"),
    path("rdetails/", ResDetails, name="reservation-details"),
]
