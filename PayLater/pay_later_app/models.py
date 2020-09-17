from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class SimplUser(models.Model):

    username = models.CharField(
        max_length=32, unique=True,
        help_text="Name of the user"
    )
    email = models.EmailField(
        max_length=64,
        help_text="Email of the user"
    )
    credit_limit = models.IntegerField(
        validators=[MinValueValidator(Decimal('0.0'))],
        help_text="Max Usable Credit Amount"
    )
    available_credit_limit = models.IntegerField(
        validators=[MinValueValidator(Decimal('0.0'))],
        help_text="Available Credit Amount"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(credit_limit__gte=0),
                name="simpluser_credit_limit_min_0_constraint",
            ),
            models.CheckConstraint(
                check=models.Q(
                    available_credit_limit__gte=0,
                    available_credit_limit__lte=models.F('credit_limit'),
                ),
                name="simpluser_available_credit_limit_constraint",
            ),
        ]

    def __str__(self):
        return f"User: {self.username} | Credit Limit: {self.credit_limit}"


class Merchant(models.Model):

    merchant_name = models.CharField(
        max_length=32, unique=True,
        help_text="Name of the merchant"
    )
    email = models.EmailField(
        max_length=64,
        help_text="Email of the merchant"
    )
    discount_rate = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.0')),
            MaxValueValidator(Decimal('100.0')),
        ],
        help_text="Discount provided by the merchant"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    discount_rate__gte=0,
                    discount_rate__lte=100,
                ),
                name="merchant_discount_rate_constraint",
            ),
        ]

    def __str__(self):
        return (
            f"Merchant: {self.merchant_name} | "
            f"Discount Rate: {self.discount_rate}"
        )


class Purchase(models.Model):

    simpluser = models.ForeignKey(
        SimplUser, on_delete=models.PROTECT,
        help_text="User who made the purchase"
    )
    merchant = models.ForeignKey(
        Merchant, on_delete=models.PROTECT,
        help_text="Merchant user made the purchase from"
    )
    # Purchases with amount 0 are allowed.
    amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.0'))],
        help_text="Purchase amount"
    )
    merchant_discount = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.0'))],
        help_text="Merchant Discount. This amount is our application fee"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(amount__gte=0),
                name="purchase_amount_min_0_constraint",
            ),
        ]

    def save(self, *args, **kwargs):
        self.merchant_discount = self.amount * self.merchant.discount_rate / 100
        return super().save(self)

    def __str__(self):
        return (
            f"User: {self.simpluser.username} | "
            f"Merchant: {self.merchant.merchant_name} | Amount: {self.amount}"
        )


class Payment(models.Model):

    simpluser = models.ForeignKey(
        SimplUser, on_delete=models.PROTECT,
        help_text="User who made the payment"
    )
    # Payments with amount 0 is allowed. This can be useful if we
    # simply want to save user's card details for future payment.
    amount = models.DecimalField(
        validators=[MinValueValidator(Decimal('0.0'))],
        max_digits=10, decimal_places=2,
        help_text="Payment amount"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(amount__gte=0),
                name="payment_amount_min_0_constraint",
            ),
        ]

    def __str__(self):
        return f"User: {self.simpluser.username} | Payment Amount: {self.amount}"
