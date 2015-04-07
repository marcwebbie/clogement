import datetime

from django.db import models
from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    BooleanField,
    IntField,
    FloatField,
    ListField,
    DateTimeField,
    EmbeddedDocumentField,
)


class Logement(EmbeddedDocument):
    type_logement = StringField()
    contrat = StringField()
    ville = StringField()

    prix = StringField()
    garantie = StringField()
    caution = FloatField()
    charges = FloatField()

    surface = IntField()
    etage = IntField()
    num_pieces = IntField()
    num_chambres = IntField()
    ascenseur = BooleanField()
    place_parking = IntField()
    climatisation = StringField()

    gardien = BooleanField()
    piscine = BooleanField()
    playground = BooleanField()
    gym = BooleanField()
    spa = BooleanField()
    espace_enfant = BooleanField()
    espace_barbecue = BooleanField()


class Cahier(Document):
    created_at = DateTimeField(default=datetime.datetime.now)
    description = StringField(required=True)
    budget = FloatField(required=True)
    villes = ListField(StringField())
    logements = ListField(EmbeddedDocumentField(Logement))
