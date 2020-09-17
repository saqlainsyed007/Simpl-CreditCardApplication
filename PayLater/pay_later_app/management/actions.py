from argparse import Action, ArgumentError

from pay_later_app.models import SimplUser, Merchant


class ValidateAndSetSimplUser(Action):
    def __call__(self, parser, args, values, option_string=None):
        try:
            setattr(
                args, self.dest, SimplUser.objects.get(username=values)
            )
        except SimplUser.DoesNotExist:
            raise ArgumentError(
                self, 'Invalid username'
            )


class ValidateAndSetMerchant(Action):
    def __call__(self, parser, args, values, option_string=None):
        try:
            setattr(
                args, self.dest, Merchant.objects.get(merchant_name=values)
            )
        except Merchant.DoesNotExist:
            raise ArgumentError(
                self, 'Invalid merchant name'
            )
