from django.core.management.base import BaseCommand
from website.models import Property, Photos, SitetextEn, SitetextRu

class Command(BaseCommand):
    help = 'Initializes database with default values for all pages'

    def handle(self, *args, **options):
        try:
            name = 'narofominsk'
            location = '55.406073, 36.685741'
            contact = '+7 909 65 75 173'
            email_id = 'info@naracottage.com'
            prop = Property.objects.create(name=name, location=location,
                                           contact=contact, email_id=email_id)
            prop.save()
            name = 'narofominsk'
            title = 'Cottage for sale near Moscow'
            about = 'Cottage for sale near Naro-Fominsk. 15 hectares of land in a protected small village. The house is 290 square meters and is made of bricks. There is an additional 100 square meter basement, and a large attic which can be turned into living space.'
            address = 'Russian Federation, Moscow Region, Naro-Fominsk'
            price_dollars = '600,000'
            price_roubles = '35,000,000'
            sitetext_en = SitetextEn.objects.create(name=name, title=title,
                                                    about=about, address=address,
                                                    price_dollars=price_dollars,
                                                    price_roubles=price_roubles)
            sitetext_en.save()
            name = 'narofominsk'
            title = 'Продается элитный коттедж под Наро-фоминском (киевское шоссе)'
            about = 'Продается коттедж по киевскому направлению в районе Наро-фоминска. Участок 15 соток в охраняемом небольшом коттеджном поселке. Дом из кирпича 290 квадратных метров плюс 100 квадратных метров цокольного этажа, возможно обустройство мансарды.'
            address = 'Московская область, Наро-Фоминский район, садовое товарищество Осень, улица Профессора Арефьева 16'
            price_dollars = '600,000'
            price_roubles = '35,000,000'
            sitetext_ru = SitetextRu.objects.create(name=name, title=title,
                                                    about=about, address=address,
                                                    price_dollars=price_dollars,
                                                    price_roubles=price_roubles)
            sitetext_ru.save()
            self.stdout.write(self.style.SUCCESS('%s property added.' % name))
        except Exception as ex:
            self.stdout.write(self.style.ERROR('Could not add %s property.' % name))
        try:
            name = 'arbatflat'
            location = '55.743355, 37.579924'
            contact = '+7 909 65 75 173'
            email_id = 'random@random.com'
            prop = Property.objects.create(name=name, location=location,
                                           contact=contact, email_id=email_id)
            prop.save()
            self.stdout.write(self.style.SUCCESS('%s property added.' % name))
        except Exception as ex:
            self.stdout.write(self.style.ERROR('Could not add %s property.' % name))
