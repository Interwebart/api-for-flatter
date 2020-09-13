from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views import CarViewSet, FightViewSet

router = DefaultRouter()
router.register("cars", CarViewSet )
router.register("Fighter", FightViewSet)
urlpatterns = router.urls