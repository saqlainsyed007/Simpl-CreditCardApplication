from django import forms

from pay_later_app.models import SimplUser


class SimplUserForm(forms.ModelForm):

    class Meta:
        model = SimplUser
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        credit_limit = cleaned_data.get("credit_limit")
        available_credit_limit = cleaned_data.get("available_credit_limit")

        if available_credit_limit > credit_limit:
            raise forms.ValidationError({
                'available_credit_limit': "Available credit limit cannot be more than credit limit"
            })
