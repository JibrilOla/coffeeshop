from django.shortcuts import render, redirect
from .models import Payment, UserWallet
from django.conf import settings
from django.contrib.auth.decorators import login_required


def initiate_payment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            amount = request.POST["amount"]
            email = request.POST["email"]
            pk = settings.PAYSTACK_PUBLIC_KEY

            payment = Payment.objects.create(
                amount=amount, email=email, user=request.user
            )
            if int(payment.amount) >= 100:
                payment.save()

                context = {
                    "payment": payment,
                    "field_values": request.POST,
                    "paystack_pub_key": pk,
                    "amount_value": payment.amount_value(),
                }
                return render(request, "csapp/make_payment.html", context)
            else:
                error_message = "Minimum recharge is 100points"
                return render(
                    request, "csapp/recharge.html", {"error_message": error_message}
                )

        return render(request, "csapp/recharge.html")
    else:
        return redirect("/login")


def verifypayment(request, ref):
    payment = Payment.objects.get(ref=ref)
    verified = payment.verifypayment()

    if verified:
        payment.verified = True
        user_wallet = UserWallet.objects.get(user=request.user)
        user_wallet.balance = user_wallet.balance + payment.amount
        user_wallet.save()
        return render(request, "csapp/success.html")

    return render(request, "csapp/success.html")


@login_required
def rechargerec(request):
    rec = Payment.objects.filter(user=request.user, verified=True).order_by(
        "-date_created"
    )
    data = {"rec": rec}
    return render(request, "csapp/recharge_rec.html", data)
