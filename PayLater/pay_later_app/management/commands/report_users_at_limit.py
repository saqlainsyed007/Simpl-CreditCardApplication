from argparse import Action, ArgumentError
from django.core.management.base import BaseCommand

from pay_later_app.management.actions import (
    ValidateAndSetSimplUser,
)
from pay_later_app.utils import report_users_at_limit


class Command(BaseCommand):

    help = 'Report users who have exhausted their credit limit'

    def handle(self, *args, **kwargs):
        report_users_at_limit()
