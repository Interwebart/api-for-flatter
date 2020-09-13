from rest_framework.serializers import ModelSerializer

from core.models import Car, Fighter


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class FighterSerializer(ModelSerializer):
    class Meta:
        model = Fighter
        fields = "__all__"