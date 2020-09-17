from django.core.management.base import BaseCommand

from pay_later_app.utils import create_new_merchant


class Command(BaseCommand):

    help = 'Create a new merchant'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--merchant_name", dest="merchant_name",
            required=True, help="Merchant name",
        )

        parser.add_argument(
            "--email", dest="email",
            required=True, help="Email",
        )

        parser.add_argument(
            "--discount_rate", dest="discount_rate", type=float,
            required=True, help="Max Usable Credit Amount",
        )

    def handle(self, *args, **kwargs):
        merchant_name = kwargs['merchant_name']
        email = kwargs['email']
        discount_rate = kwargs['discount_rate']
        create_new_merchant(merchant_name, email, discount_rate)
