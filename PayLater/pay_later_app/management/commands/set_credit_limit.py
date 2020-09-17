from argparse import Action, ArgumentError
from django.core.management.base import BaseCommand

from pay_later_app.management.actions import (
    ValidateAndSetSimplUser
)
from pay_later_app.utils import set_credit_limit


class Command(BaseCommand):

    help = 'Update credit limit for a user'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--username", dest="simpluser", required=True,
            action=ValidateAndSetSimplUser, help="Username",
        )

        parser.add_argument(
            "--new_limit", dest="new_limit", required=True,
            help="New credit limit", type=float,
        )

    def handle(self, *args, **kwargs):
        simpluser = kwargs['simpluser']
        new_limit = kwargs['new_limit']
        set_credit_limit(simpluser, new_limit)
