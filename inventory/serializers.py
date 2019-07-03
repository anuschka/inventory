from rest_framework import serializers

from .models import Product, Batch, Order

class OrderSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Order
        fields = '__all__'

## is_valid method

class BatchSerializer(serializers.ModelSerializer):
    batch_in_order = OrderSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Batch
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_in_batch = BatchSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Product
        fields = '__all__'
