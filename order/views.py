from django.shortcuts import render, redirect
from .models import Order
from .models import Checkout
from django.db.models import Sum
from payments.models import UserWallet


def SelectOrder(request, price, name):
    if request.user.is_authenticated:
        myorder = Order.objects.create(
            user=request.user, product_name=name, price=price, quantity="1"
        )
        myorder.save()
        return render(
            request,
            "csapp/menu.html",
        )
    else:
        return redirect("/login")


def Cart(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)

        # Get the total withdrawal amount by each user
        order_total = (
            Order.objects.filter(user=request.user)
            .aggregate(Sum("price", default=0))
            .get("price__sum", 0.00)
        )
        orders = Order.objects.filter(user=request.user)

        # group the orders by the product name and calculate the total quantity and price
        products = orders.values("product_name").annotate(
            total_quantity=Sum("quantity"), total_price=Sum("price")
        )
        data = {"order_total": order_total, "orders": orders, "products": products}
        # pass the products to the template
        return render(request, "csapp/cart.html", data)
    else:
        return redirect("/login")


def delete_order(request, id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=id)  # get the order by its id
        order.delete()  # delete the order
        return redirect("/cart")
    else:
        return redirect("/login")


def Out(request):
    if request.user.is_authenticated:
        user_wallet = UserWallet.objects.get(user=request.user)
        orders = Order.objects.filter(user=request.user)
        distinct_products = orders.values("product_name").distinct()

        products = []
        for product in distinct_products:
            quantity = (
                orders.filter(product_name=product["product_name"])
                .aggregate(Sum("quantity"))
                .get("quantity__sum", 0)
            )
            price = (
                orders.filter(product_name=product["product_name"])
                .aggregate(Sum("price"))
                .get("price__sum", 0)
            )

            products.append(
                {
                    "": product["product_name"],
                    "Qty": quantity,
                    "Price": price,
                }
            )

        item_total = orders.aggregate(Sum("quantity", default=0)).get(
            "quantity__sum", 0.00
        )
        order_total = (
            Order.objects.filter(user=request.user)
            .aggregate(Sum("price", default=0))
            .get("price__sum", 0.00)
        )
        if request.method == "POST":
            email = request.POST.get("email")
            address = request.POST.get("address")
            number = request.POST.get("number")
            zipcode = request.POST.get("zipcode")
            payment_method = request.POST.get("payment_method")
            state = request.POST.get("state")
            city = request.POST.get("city")

            if payment_method == "PAY WITH POINTS":
                if user_wallet.balance >= order_total:
                    user_wallet.balance -= order_total
                    user_wallet.save()
                else:
                    return render(request, "csapp/failed.html")
            checkout_order = Checkout.objects.create(
                user=request.user,
                email=email,
                address=address,
                number=number,
                totalx=order_total,
                city=city,
                state=state,
                zipcode=zipcode,
                payment_method=payment_method,
                products=products,
            )
            checkout_order.save()
            Order.objects.filter(user=request.user).delete()
            return render(request, "csapp/ss.html")

        return render(
            request,
            "csapp/checkout.html",
            {"order_total": order_total, "orders": orders, "item_total": item_total},
        )

    else:
        return redirect("/login")


def orders(request):
    if request.user.is_authenticated:
        orders = Checkout.objects.filter(user=request.user).order_by("-date")
        return render(request, "csapp/orders.html", {"orders": orders})
    else:
        return redirect("/login")
