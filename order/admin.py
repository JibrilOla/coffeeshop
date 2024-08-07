from django.contrib import admin

# Register your models here.

from .models import Checkout
from django.contrib import admin



@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "date",
        "address",
        "city",
        "state",
        "zipcode",
        "number",
        "email",
        "date",
        "totalx",
        "payment_method",
        "status",
    ]
    list_filter = ("status",)
    actions = ["complete_orders"]

    def save_model(self, request, obj, form, change):
        if obj.status == "Completed":
            pass

        super().save_model(request, obj, form, change)

    def complete_orders(self, request, queryset):
        queryset.update(status="Completed")
        self.message_user(request, "Selected Orders have been completed successfully.")

    complete_orders.short_description = "Check completed Orders"

