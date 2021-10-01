from rest_framework import serializers
from .models import Electronics


class electronicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronics
        fields = '__all__'