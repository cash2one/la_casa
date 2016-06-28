from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from website.models import Property, SitetextEn


def home(request):
    prop = Property.objects.get(name='narofominsk')
    template = loader.get_template('naracottage_home.html')
    location = prop.location
    latitude, longitude = location.split(',')
    sitetext_en = SitetextEn.objects.get(name='narofominsk')
    context = {
                'logo_url': 'images/logo_naracottage.png',
                'latitude': latitude,
                'longitude': longitude,
                'phone': prop.contact,
                'title': sitetext_en.title,
                'about': sitetext_en.about,
                'address': sitetext_en.address,
                'price_dollars': sitetext_en.price_dollars,
                'price_roubles': sitetext_en.price_roubles
              }
    return HttpResponse(template.render(context, request))
