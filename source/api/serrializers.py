from rest_framework import serializers

from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


# class OrderProductSerrializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)
#
#     class Meta:
#         model = OrderProduct
#         fields = '__all__'
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     order_products = OrderProductSerrializer(many=True, read_only=True)
#
#     class Meta:
#         model = Order
#         fields = ['order_products', 'address', 'phone', 'name']
