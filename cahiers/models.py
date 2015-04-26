from uuid import uuid4

from django.db import models

from accounts.models import Profile


class Cahier(models.Model):
    profile = models.ForeignKey(Profile)
    description = models.CharField(max_length=255)
    budget = models.FloatField(max_length=255)

    class Meta:
        permissions = (
            ('view_cahier', 'View Cahier'),
            ('edit_cahier', 'Edit Cahier'),
        )

    def __str__(self):
        return self.description


class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


class Logement(models.Model):
    cahier = models.ForeignKey(Cahier, related_name='logements')

    # Geo
    city = models.ForeignKey(City)
    area = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)

    # Finances
    price = models.FloatField()
    warrant = models.FloatField(default=0, null=False, blank=False)
    caution = models.FloatField(default=0, null=False, blank=False)
    charges = models.FloatField(default=0, null=False, blank=False)

    # Espace
    surface = models.IntegerField()
    floor = models.IntegerField(null=True, blank=True)
    num_room = models.IntegerField(default=1)
    num_bedroom = models.IntegerField(default=0)
    elevator = models.IntegerField()
    num_parking = models.IntegerField()

    # Atouts
    climatisation = models.BooleanField()
    water_purifier = models.BooleanField()
    balcon = models.BooleanField()
    garden = models.BooleanField()

    # Immeuble
    gardien = models.BooleanField()
    swimming_pool = models.BooleanField()
    playground = models.BooleanField()
    gym = models.BooleanField()
    spa = models.BooleanField()
    barbecue_area = models.BooleanField()

    # Resourses
    url = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return "{}, {}m2, Price: {}".format(self.city, self.surface, self.price)


class LogementPhoto(models.Model):
    logement = models.ForeignKey(Logement)
    description = models.CharField(max_length=255, null=True, blank=True)
