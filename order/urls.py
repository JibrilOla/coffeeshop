from django.urls import path
from .views import *

app_name = "order"
urlpatterns = [
    path("order/<str:name>/<int:price>/", SelectOrder, name="Order"),
    path("cart/", Cart, name="Cart"),
    path("delete_order/<int:id>/", delete_order, name="delete_order"),
    path("checkout/", Out, name="checkout"),
    path("orders/", orders, name="orders"),
]
