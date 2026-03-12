from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MeasurementCreateView

router = DefaultRouter()
router.register('sensors', SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('measurements/', MeasurementCreateView.as_view()),
]