from django.core.management.base import BaseCommand

from pay_later_app.utils import create_new_user


class Command(BaseCommand):

    help = 'Create a new user'

    def add_arguments(self, parser):
        super().add_arguments(parser)

        parser.add_argument(
            "--username", dest="username",
            required=True, help="Username",
        )

        parser.add_argument(
            "--email", dest="email",
            required=True, help="Email",
        )

        parser.add_argument(
            "--credit_limit", dest="credit_limit", type=int,
            required=True, help="Max usable credit amount",
        )

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        credit_limit = kwargs['credit_limit']
        create_new_user(username, email, credit_limit)
