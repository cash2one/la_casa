from django.core.management.base import BaseCommand
from website.models import Property, Photos, SitetextEn, SitetextRu

LOREM_TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

class Command(BaseCommand):
    help = 'Initializes database with default values for all pages'

    def handle(self, *args, **options):
        try:
            name = 'narofominsk'
            location = '55.406073, 36.685741'
            contact = '1234567890'
            email_id = 'random@random.com'
            prop = Property.objects.create(name=name, location=location,
                                           contact=contact, email_id=email_id)
            prop.save()
            name = 'narofominsk'
            title = 'Beautiful flat for sale at Narofominsk'
            about = LOREM_TEXT
            address = 'Russia, Moscow Region, NaroFominsk, Tureyka Village, Profesora Arefieva Street, 1'
            price_dollars = 600000
            price_roubles = 600000
            sitetext_en = SitetextEn.objects.create(name=name, title=title,
                                                  about=about, address=address,
                                                  price_dollars=price_dollars,
                                                  price_roubles=price_roubles)
            sitetext_en.save()
            self.stdout.write(self.style.SUCCESS('%s property added.' % name))
        except Exception as ex:
            self.stdout.write(self.style.ERROR('Could not add %s property.' % name))
        try:
            name = 'arbatflat'
            location = '55.743355, 37.579924'
            contact = '1234567890'
            email_id = 'random@random.com'
            prop = Property.objects.create(name=name, location=location,
                                           contact=contact, email_id=email_id)
            prop.save()
            self.stdout.write(self.style.SUCCESS('%s property added.' % name))
        except Exception as ex:
            self.stdout.write(self.style.ERROR('Could not add %s property.' % name))

