from uuid import uuid4

from django.db import models


class Cahier(models.Model):
    description = models.CharField(max_length=255)
    budget = models.FloatField(max_length=255)

    def __str__(self):
        return self.description

class Pays(models.Model):
    nom = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Pays'

    def __str__(self):
        return self.nom


class Ville(models.Model):
    nom = models.CharField(max_length=255)
    pays = models.ForeignKey(Pays)

    def __str__(self):
        return self.nom


class Logement(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    cahier = models.ForeignKey(Cahier, related_name='logements')

    # Geo
    ville = models.ForeignKey(Ville)
    quartier = models.CharField(max_length=255, null=True, blank=True)
    code_postal = models.CharField(max_length=255, null=True, blank=True)

    # Finances
    prix = models.FloatField()
    garantie = models.FloatField(default=0, null=False, blank=False)
    caution = models.FloatField(default=0, null=False, blank=False)
    charges = models.FloatField(default=0, null=False, blank=False)

    # Espace
    surface = models.IntegerField()
    etage = models.IntegerField(null=True, blank=True)
    num_pieces = models.IntegerField(default=1)
    num_chambres = models.IntegerField(default=0)
    ascenseur = models.IntegerField()
    num_places_parking = models.IntegerField()

    # Atouts
    climatisation = models.BooleanField()
    purificateur_eau = models.BooleanField()
    balcon = models.BooleanField()
    jardin = models.BooleanField()

    # Immeuble
    gardien = models.BooleanField()
    piscine = models.BooleanField()
    playground = models.BooleanField()
    gym = models.BooleanField()
    spa = models.BooleanField()
    espace_enfant = models.BooleanField()
    espace_barbecue = models.BooleanField()

    # Resourses
    url = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return "{}, {}".format(self.ville, self.prix)
