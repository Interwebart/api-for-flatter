from django.http import JsonResponse
from rest_framework.viewsets import ViewSet, ModelViewSet

from core.models import Car, Fighter
from core.serializers import CarSerializer, FighterSerializer

class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class FightViewSet(ModelViewSet):
    serializer_class = FighterSerializer
    queryset = Fighter.objects.all()
