
from pay_later_app.models import SimplUser, Merchant, Purchase, Payment
from pay_later_app.utils import (
    create_new_user, create_new_merchant, make_purchase, make_payment,
    report_discounts, report_dues, report_users_at_limit, set_credit_limit,
    set_discount_rate,
)


Payment.objects.all().delete()
Purchase.objects.all().delete()
SimplUser.objects.all().delete()
Merchant.objects.all().delete()

print("Creating users...")
user_1 = create_new_user('Amado', 'amado@test.simpl.com', 20000)
user_2 = create_new_user('Alejandro', 'alejandro@test.simpl.com', 10000)
user_3 = create_new_user('Julee', 'julee@test.simpl.com', 12000)
print("")

print("Creating merchants...")
merchant_1 = create_new_merchant('Amazon', 'amazon@support.test.simpl.com', 1.5)
merchant_2 = create_new_merchant('Flipkart', 'flipkart@support.test.simpl.com', 2.4)
merchant_3 = create_new_merchant('Myntra', 'myntra@support.test.simpl.com', 1.6)
print("")

print(f"{user_1.username} shopping...")
make_purchase(user_1, merchant_1, 10000)
make_purchase(user_1, merchant_2, 5000)
make_purchase(user_1, merchant_2, 10000)
print("")

print(f"{user_2.username} shopping...")
make_purchase(user_2, merchant_2, 7000)
make_purchase(user_2, merchant_3, 3000)
make_purchase(user_2, merchant_3, 4000)
print("")

print(f"{user_3.username} shopping...")
make_purchase(user_3, merchant_3, 5000)
make_purchase(user_3, merchant_1, 2000)
make_purchase(user_3, merchant_3, 5000)
make_purchase(user_3, merchant_3, 3000)
print("")

print(f"{user_1.username} paying bills...")
make_payment(user_1, 5000)
make_payment(user_1, 10000)
make_payment(user_1, 10000)
print("")

print("Reporting all discounts...")
report_discounts()
print("")

print("Reporting individual discounts...")
report_discounts(merchant_1)
report_discounts(merchant_2)
report_discounts(merchant_3)
print("")

print("Reporting all dues...")
report_dues()
print("")

print("Reporting individual dues...")
report_dues(user_1)
report_dues(user_2)
report_dues(user_3)
print("")

print("Reporting users at limit...")
report_users_at_limit()
print("")

print(f"Setting limit for {user_3.username}...")
set_credit_limit(user_3, 10000)
set_credit_limit(user_3, 15000)
print("")

print(f"Reporting dues for {user_3.username}...")
report_dues(user_3)
print("")

print("Reporting users at limit...")
report_users_at_limit()
print("")

print(f"Setting new discount rate for {merchant_1.merchant_name}...")
set_discount_rate(merchant_1, 2.0)
print("")

print(f"Making purchases at {merchant_1.merchant_name}...")
make_purchase(user_3, merchant_1, 3000)
print("")

print(f"Reporting discounts for {merchant_1.merchant_name}...")
report_discounts(merchant_1)
print("")

print("Reporting users at limit...")
report_users_at_limit()
print("")
