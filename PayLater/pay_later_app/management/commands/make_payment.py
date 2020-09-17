from argparse import Action, ArgumentError
from django.core.management.base import BaseCommand

from pay_later_app.management.actions import (
    ValidateAndSetSimplUser,
)
from pay_later_app.utils import make_payment


class Command(BaseCommand):

    help = 'Make a payment'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--username", dest="simpluser", required=True,
            action=ValidateAndSetSimplUser, help="Username",
        )

        parser.add_argument(
            "--amount", dest="amount", required=True,
            help="Payment amount", type=float,
        )

    def handle(self, *args, **kwargs):
        simpluser = kwargs['simpluser']
        amount = kwargs['amount']
        make_payment(simpluser, amount)
