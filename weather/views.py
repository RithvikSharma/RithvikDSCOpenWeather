from django.shortcuts import render
from django.http import JsonResponse
import requests


def input_city(request):
    return render(request, 'input.html', {})


def display_weather(request, city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=f0f84f880b24c77158a4eb8b327f2c28')
    return JsonResponse(r.json())
