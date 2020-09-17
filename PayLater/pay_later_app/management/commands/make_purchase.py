from argparse import Action, ArgumentError
from django.core.management.base import BaseCommand

from pay_later_app.management.actions import (
    ValidateAndSetSimplUser, ValidateAndSetMerchant
)
from pay_later_app.utils import make_purchase


class Command(BaseCommand):

    help = 'Make a purchase'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--username", dest="simpluser", required=True,
            action=ValidateAndSetSimplUser, help="Username",
        )

        parser.add_argument(
            "--merchant_name", dest="merchant", required=True,
            action=ValidateAndSetMerchant, help="Merchant name",
        )

        parser.add_argument(
            "--amount", dest="amount", required=True,
            help="Purchase amount", type=float,
        )

    def handle(self, *args, **kwargs):
        simpluser = kwargs['simpluser']
        merchant = kwargs['merchant']
        amount = kwargs['amount']
        make_purchase(simpluser, merchant, amount)
