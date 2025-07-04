import datetime

import requests as re
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from weather.forms import InputForm


# Create your views here.
def home(request):
    form = None
    show_weather_flag = False
    country = None
    temp = None
    city = None
    icon = None
    description = None
    current_time = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city_input']
            weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aec4d29e3bf94398cde24c65c9801dc1'
            try:
                data = re.get(weather_url, params={'units': 'metric'}).json()
                description = data['weather'][0]['description']
                icon = data['weather'][0]['icon']
                temp = data['main']['temp']
                country = data['sys']['country']
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                show_weather_flag = True
            except:
                messages.error(request,'could not find the city')
    if request.method == 'GET':
        form = InputForm()
    context = {
        'form': form,
        'show_weather_flag': show_weather_flag,
        'current_time': current_time,
        'country': country,
        'temp': temp,
        'city': city,
        'icon': icon,
        'description': description,
    }
    return render(request,'html/home.html',context)
