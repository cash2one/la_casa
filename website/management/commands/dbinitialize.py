from django.core.management.base import BaseCommand
from website.models import Property, Photos, Sitetext


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

