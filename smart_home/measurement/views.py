from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .models import Sensor, Measurement
from .serializers import (
    SensorSerializer,
    SensorDetailSerializer,
    MeasurementSerializer,
    MeasurementCreateSerializer
)


class SensorViewSet(ModelViewSet):

    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        return SensorSerializer


class MeasurementCreateView(CreateAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer
