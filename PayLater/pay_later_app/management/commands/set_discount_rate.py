from argparse import Action, ArgumentError
from django.core.management.base import BaseCommand

from pay_later_app.management.actions import (
    ValidateAndSetMerchant
)
from pay_later_app.utils import set_discount_rate


class Command(BaseCommand):

    help = 'Set a new discount rate for a merchant'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--merchant_name", dest="merchant", required=True,
            action=ValidateAndSetMerchant, help="Merchant name",
        )

        parser.add_argument(
            "--discount_rate", dest="discount_rate", required=True,
            help="Merchant discount rate", type=float,
        )

    def handle(self, *args, **kwargs):
        merchant = kwargs['merchant']
        discount_rate = kwargs['discount_rate']
        set_discount_rate(merchant, discount_rate)
