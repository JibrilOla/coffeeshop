from bootstrap_colors.views import BootstrapColorsView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("csapp.urls", namespace="csapp")),
    path("", include("registration.urls", namespace="registration")),
    path("", include("order.urls", namespace="order")),
    path("", include("payments.urls", namespace="payments")),
    path("", include("reservations.urls", namespace="reservations")),
    path("colors.css", BootstrapColorsView.as_view(), name="colors"),
    path("", include("django.contrib.auth.urls")),
]
