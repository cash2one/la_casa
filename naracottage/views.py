from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from website.models import Property


def home(request):
    prop = Property.objects.get(name='narofominsk')
    template = loader.get_template('naracottage_home.html')
    location = prop.location
    latitude, longitude = location.split(',')
    context = {
                'name': prop.name,
                'latitude': latitude,
                'longitude': longitude,
                'phone': prop.contact,
              }
    return HttpResponse(template.render(context, request))
