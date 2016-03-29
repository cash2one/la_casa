from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    location = models.CharField(max_length=100)
    price_rouble = models.IntegerField()
    price_usd = models.IntegerField()
    contact = models.CharField(max_length=15)
    email_id = models.EmailField()

    def __unicode__(self):
        return unicode(self.id)


class Photos(models.Model):
    name = models.CharField(max_length=30)
    photo = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.id)


class Sitetext(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    section = models.CharField(max_length=15)
    language = models.CharField(max_length=5)

    def __unicode__(self):
        return unicode(self.id)
