from rest_framework import serializers
from .models import Sneaker

class SneakerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    description = serializers.CharField(max_length=128)
    price = serializers.IntegerField()
    image = serializers.ImageField()

    def create(self, data):
        return Sneaker.objects.create(**data)
