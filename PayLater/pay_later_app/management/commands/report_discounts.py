from argparse import Action, ArgumentError
from django.core.management.base import BaseCommand

from pay_later_app.management.actions import (
    ValidateAndSetMerchant,
)
from pay_later_app.utils import report_discounts


class Command(BaseCommand):

    help = 'Report discounts earned from merchants'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--merchant_name", dest="merchant", required=False,
            action=ValidateAndSetMerchant, help="Merchant name",
        )

    def handle(self, *args, **kwargs):
        merchant = kwargs.get('merchant')
        report_discounts(merchant)
