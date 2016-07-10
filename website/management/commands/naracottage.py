# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from website.models import Property, Photos, SitetextEn, SitetextRu
import os

NAME = 'narofominsk'

class Command(BaseCommand):
    help = 'Initializes database with default values for all pages of Naracottage'

    def handle(self, *args, **options):
        location = '55.406073, 36.685741'
        contact = '+7 909 65 75 173'
        email_id = 'info@naracottage.com'
        prop = Property.objects.create(name=NAME, location=location,
                                       contact=contact, email_id=email_id)
        prop.save()
        static_path = 'static/images/naracottage'
        absolute_path = os.path.abspath(static_path)
        photos = os.listdir(absolute_path)
        for photo in photos:
            # .zip file should not be added to Database.
            if '.zip' in photo:
                pass
            photo_path = '/%s/%s' % (static_path, photo)
            photo_alt = photo
            photo_model_obj = Photos.objects.create(name=NAME,
                                                    photo=photo_path,
                                                    alt_name=photo_alt)
            photo_model_obj.save()
        title = 'Cottage for sale near Moscow'
        about = 'Cottage for sale near Naro-Fominsk. 15 hectares of land in a protected small village. The house is 290 square meters and is made of bricks. There is an additional 100 square meter basement, and a large attic which can be turned into living space.'
        address = 'Russian Federation, Moscow Region, Naro-Fominsk'
        price_euros = '600,000'
        price_roubles = '35,000,000'
        sitetext_en = SitetextEn.objects.create(name=NAME, title=title,
                                                about=about, address=address,
                                                price_euros=price_euros,
                                                price_roubles=price_roubles)
        sitetext_en.save()
        title = 'Продается элитный коттедж под Наро-фоминском (киевское шоссе)'
        about = 'Продается коттедж по киевскому направлению в районе Наро-фоминска. Участок 15 соток в охраняемом небольшом коттеджном поселке. Дом из кирпича 290 квадратных метров плюс 100 квадратных метров цокольного этажа, возможно обустройство мансарды.'
        address = 'Московская область, Наро-Фоминский район, садовое товарищество Осень, улица Профессора Арефьева 16'
        price_euros = '600,000'
        price_roubles = '35,000,000'
        sitetext_ru = SitetextRu.objects.create(name=NAME, title=title,
                                                about=about, address=address,
                                                price_euros=price_euros,
                                                price_roubles=price_roubles)
        sitetext_ru.save()
        self.stdout.write(self.style.SUCCESS('%s property added.' % NAME))

