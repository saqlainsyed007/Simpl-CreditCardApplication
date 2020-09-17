from argparse import Action, ArgumentError
from django.core.management.base import BaseCommand

from pay_later_app.management.actions import (
    ValidateAndSetSimplUser,
)
from pay_later_app.utils import report_dues


class Command(BaseCommand):

    help = 'Report dues of users'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--username", dest="simpluser", required=False,
            action=ValidateAndSetSimplUser, help="Username",
        )

    def handle(self, *args, **kwargs):
        simpluser = kwargs.get('simpluser')
        report_dues(simpluser)
