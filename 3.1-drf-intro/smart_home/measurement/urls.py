from django.urls import path

from .views import MeasurementApiView, SensorApiView, SensorDetailApiView


urlpatterns = [
    path('measurement/', MeasurementApiView.as_view()),
    path('sensor/', SensorApiView.as_view()),
    path('sensor/<int:pk>/', SensorDetailApiView.as_view()),
]
