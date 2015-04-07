from tastypie.resources import ModelResource

from .models import Cahier, Logement, Pays, Ville


class CahierResource(ModelResource):

    class Meta:
        queryset = Cahier.objects.all()


class LogementResource(ModelResource):

    class Meta:
        queryset = Logement.objects.all()


class PaysResource(ModelResource):

    class Meta:
        queryset = Pays.objects.all()


class VilleResource(ModelResource):

    class Meta:
        queryset = Ville.objects.all()
