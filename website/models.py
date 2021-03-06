from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=25)
    email_id = models.EmailField()

    def __unicode__(self):
        return unicode(self.id)


class Photos(models.Model):
    name = models.CharField(max_length=30)
    alt_name = models.CharField(max_length=100)
    # Make this photo_path and correct initialization script and views.py
    photo = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.id)


class SitetextEn(models.Model):
    name = models.CharField(max_length=30)
    title = models.TextField()
    about = models.TextField()
    address = models.TextField()
    price_euros = models.CharField(max_length=15)
    price_roubles = models.CharField(max_length=15)

    def __unicode__(self):
        return unicode(self.id)

class SitetextRu(models.Model):
    name = models.CharField(max_length=30)
    title = models.TextField()
    about = models.TextField()
    address = models.TextField()
    price_euros = models.CharField(max_length=15)
    price_roubles = models.CharField(max_length=15)

    def __unicode__(self):
        return unicode(self.id)

