from django.urls import path
from .views import *

app_name = "registration"
urlpatterns = [
    path("register/", Register, name="register"),
    path("login/", Login, name="login"),
    path("dashboard/", Dashboard, name="dashboard"),
]
