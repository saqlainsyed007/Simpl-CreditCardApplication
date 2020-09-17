from django.contrib import admin

from pay_later_app.forms import SimplUserForm
from pay_later_app.models import SimplUser, Merchant, Purchase, Payment


class SimplUserAdmin(admin.ModelAdmin):

    model = SimplUser
    form = SimplUserForm

    list_display = (
        "username", "email", "credit_limit",
        "created", "updated",
    )
    search_fields = (
        "username", "email",
    )
    list_filter = (
        "created", "updated",
    )
    readonly_fields = ("created", "updated", )


class MerchantAdmin(admin.ModelAdmin):

    model = Merchant

    list_display = (
        "merchant_name", "email", "discount_rate",
        "created", "updated",
    )
    search_fields = (
        "merchant_name", "email",
    )
    list_filter = (
        "created", "updated",
    )
    readonly_fields = ("created", "updated", )


class PurchaseAdmin(admin.ModelAdmin):

    model = Purchase

    list_display = (
        "simpluser", "merchant", "amount",
        "created", "updated",
    )
    search_fields = (
        "simpluser__username", "merchant__merchant_name",
    )
    list_filter = (
        "created", "updated",
    )
    readonly_fields = ("created", "updated", )


class PaymentAdmin(admin.ModelAdmin):

    model = Payment

    list_display = (
        "simpluser", "amount",
        "created", "updated",
    )
    search_fields = (
        "simpluser__username",
    )
    list_filter = (
        "created", "updated",
    )
    readonly_fields = ("created", "updated", )


admin.site.register(SimplUser, SimplUserAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Payment, PaymentAdmin)
