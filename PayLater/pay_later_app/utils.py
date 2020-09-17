from django.db import transaction
from django.db.models import F, Sum

from pay_later_app.serializers import (
    SimplUserSerializer, MerchantSerializer,
    PurchaseSerializer, PaymentSerializer,
)
from pay_later_app.models import SimplUser, Merchant, Purchase, Payment


def print_serializer_errors(serializer_obj, data):
    for field in serializer_obj.errors:
        print(f"{field}" + (f": {data[field]}" if data.get(field) else ""))
        for error in serializer_obj.errors[field]:
            print(f" - {str(error)}")


def create_new_user(username, email, credit_limit):
    new_user_data = {
        "username": username,
        "email": email,
        "credit_limit": credit_limit,
        "available_credit_limit": credit_limit,
    }
    new_user_serializer = SimplUserSerializer(data=new_user_data)
    if new_user_serializer.is_valid():
        new_user = new_user_serializer.save()
        print(f"User {username} created!")
        return new_user
    print_serializer_errors(new_user_serializer, new_user_data)
    return


def set_credit_limit(simpluser, new_limit):
    due_amount = simpluser.credit_limit - simpluser.available_credit_limit
    if not 0 <= due_amount < new_limit:
        print(f"Error! Limit cannot be reduced below due amount({due_amount}) or 0")
        return
    increase = new_limit - simpluser.credit_limit
    simpluser.available_credit_limit += increase
    simpluser.credit_limit = new_limit
    simpluser.save()
    print(f"Success! New credit limit for {simpluser.username} is {new_limit}")
    return simpluser


def create_new_merchant(merchant_name, email, discount_rate):
    new_merchant_data = {
        "merchant_name": merchant_name,
        "email": email,
        "discount_rate": discount_rate,
    }
    new_merchant_serializer = MerchantSerializer(data=new_merchant_data)
    if new_merchant_serializer.is_valid():
        new_merchant = new_merchant_serializer.save()
        print(f"Merchant {merchant_name} created!")
        return new_merchant
    print_serializer_errors(new_merchant_serializer, new_merchant_data)
    return


def set_discount_rate(merchant, new_discount_rate):
    if new_discount_rate < 0:
        print(f"Error! Discount rate must be greater than or equal to 0")
        return
    merchant.discount_rate = new_discount_rate
    merchant.save()
    print(
        f"Success! New discount rate for {merchant.merchant_name} "
        f"is {new_discount_rate}"
    )
    return merchant


@transaction.atomic
def make_purchase(simpluser, merchant, amount):
    purchase_data = {
        "simpluser": simpluser.pk,
        "merchant": merchant.pk,
        "amount": amount,
    }
    purchase_serializer = PurchaseSerializer(data=purchase_data)
    if not purchase_serializer.is_valid():
        print_serializer_errors(purchase_serializer, purchase_data)
        return
    if amount > simpluser.available_credit_limit:
        print(
            f"Rejected! Amount({amount}) cannot be higher than available "
            f"credit limit({simpluser.available_credit_limit})"
        )
        return
    purchase_serializer.save()
    simpluser.available_credit_limit -= amount
    simpluser.save()
    print(
        f"Transaction Successful! {simpluser.username} purchased goods worth "
        f"{amount} from {merchant.merchant_name}. Available credit limit for "
        f"{simpluser.username} is {simpluser.available_credit_limit}"
    )
    return


@transaction.atomic
def make_payment(simpluser, amount):
    payment_data = {
        "simpluser": simpluser.pk,
        "amount": amount,
    }
    payment_serializer = PaymentSerializer(data=payment_data)
    if not payment_serializer.is_valid():
        print_serializer_errors(payment_serializer, payment_data)
        return
    payable_amount = simpluser.credit_limit - simpluser.available_credit_limit
    if amount > payable_amount:
        print(
            f"Rejected! Payment amount({amount}) cannot be higher than "
            f"payable amount ({payable_amount})"
        )
        return

    payment_serializer.save()
    simpluser.available_credit_limit += amount
    simpluser.save()
    print(
        f"Transaction Successful! An amount of {amount} has been "
        f"successfully credited to {simpluser.username}. Available "
        f"credit limit is {simpluser.available_credit_limit}"
    )
    return


def report_discounts(merchant=None):
    filter_dict = {}
    if merchant:
        filter_dict = {'merchant': merchant}
    merchant_discounts = Purchase.objects.filter(
        **filter_dict
    ).values(
        merchant_name=F('merchant__merchant_name'),
    ).annotate(
        discount=Sum('merchant_discount')
    )
    for merchant_discount in merchant_discounts:
        print(
            f"{merchant_discount['merchant_name']}: "
            f"{merchant_discount['discount']}"
        )
    return merchant_discounts


def report_dues(simpluser=None):
    filter_dict = {}
    if simpluser:
        filter_dict = {'id': simpluser.id}
    dues = SimplUser.objects.filter(
        **filter_dict
    ).values(
        'username'
    ).annotate(
        due_amount=F('credit_limit') - F('available_credit_limit')
    )
    for due in dues:
        print(
            f"{due['username']}: "
            f"{due['due_amount']}"
        )
    return dues


def report_users_at_limit():
    users_at_limit = SimplUser.objects.filter(
        available_credit_limit=0
    ).values_list('username', flat=True)
    print(*users_at_limit, sep="\n")
