from rest_framework import generics

from .models import Measurement, Sensor
from .serializers import MeasurementCreateSerializer, SensorDetailSerializer, SensorSerializer


class SensorApiView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailApiView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementApiView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer
