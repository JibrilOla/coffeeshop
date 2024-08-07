from django.contrib import admin
from .models import Payment, UserWallet
from django.contrib.auth.models import User
from django.contrib import admin


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "ref", "amount", "verified", "date_created"]


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


class UserWalletInline(admin.TabularInline):
    model = UserWallet
    fk_name = "user"
    extra = 0


admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserWallet)
admin.site.unregister(User)
