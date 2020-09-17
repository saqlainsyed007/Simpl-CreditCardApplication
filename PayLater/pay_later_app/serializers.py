from rest_framework import serializers

from pay_later_app.models import SimplUser, Merchant, Purchase, Payment


class SimplUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimplUser
        fields = '__all__'

    def validate(self, data):
        validated_data = super().validate(data)
        credit_limit = validated_data['credit_limit']
        available_credit_limit = validated_data['available_credit_limit']
        if available_credit_limit > credit_limit:
            raise serializers.ValidationError({
                "available_credit_limit": (
                    f"This value cannot be greater than credit_limit({credit_limit})"
                )
            })
        return validated_data


class MerchantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Merchant
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        exclude = ['merchant_discount']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
