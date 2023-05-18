from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:location>', views.display_weather_info, name='weather-info')
]