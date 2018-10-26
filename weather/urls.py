from django.urls import path
from weather import views

urlpatterns = [
    path('', views.input_city, name='input'),
    path('<slug:city>/', views.display_weather, name='weather')
]
