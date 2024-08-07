from django.contrib import admin

from .models import Reservation
from django.contrib import admin


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "name",
        "email",
        "persons",
        "time",
        "date",
        "date_placed",
    ]
