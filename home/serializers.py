from rest_framework import serializers
from .models import Wardrobe

class WardrobeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wardrobe
        fields = '__all__'