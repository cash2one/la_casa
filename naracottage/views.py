from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from website.models import Property, SitetextRu, SitetextEn, Photos


def home_ru(request):
    prop = Property.objects.get(name='narofominsk')
    template = loader.get_template('naracottage_ru.html')
    location = prop.location
    latitude, longitude = location.split(',')
    photos = Photos.objects.filter(name='narofominsk')
    photo_map = {}
    for photo in photos:
        photo_map[photo.alt_name] = photo.photo
    sitetext_ru = SitetextRu.objects.get(name='narofominsk')
    context = {
                'logo_url': 'images/logo_naracottage.png',
                'latitude': latitude,
                'longitude': longitude,
                'phone': prop.contact,
                'title': sitetext_ru.title,
                'about': sitetext_ru.about,
                'address': sitetext_ru.address,
                'price_euros': sitetext_ru.price_euros,
                'price_roubles': sitetext_ru.price_roubles,
                'photo_map': photo_map
              }
    return HttpResponse(template.render(context, request))


def home_en(request):
    prop = Property.objects.get(name='narofominsk')
    template = loader.get_template('naracottage_en.html')
    location = prop.location
    latitude, longitude = location.split(',')
    photos = Photos.objects.filter(name='narofominsk')
    photo_map = {}
    for photo in photos:
        photo_map[photo.alt_name] = photo.photo
    sitetext_en = SitetextEn.objects.get(name='narofominsk')
    context = {
                'logo_url': 'images/logo_naracottage.png',
                'latitude': latitude,
                'longitude': longitude,
                'phone': prop.contact,
                'title': sitetext_en.title,
                'about': sitetext_en.about,
                'address': sitetext_en.address,
                'price_euros': sitetext_en.price_euros,
                'price_roubles': sitetext_en.price_roubles,
                'photo_map': photo_map
              }
    return HttpResponse(template.render(context, request))

