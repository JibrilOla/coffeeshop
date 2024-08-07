from django.urls import path
from .views import *

app_name = "csapp"
urlpatterns = [
    path("", Home, name="home"),
    path("home/", Home, name="home"),
    path("about/", About, name="about"),
    path("service/", Service, name="service"),
    path("menu/", Menu, name="menu"),
    path("testimonial/", Testimonial, name="testimonial"),
    path("dashboard/", Dashboard, name="dashboard"),
]
