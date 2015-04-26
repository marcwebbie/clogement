from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cahiers.models import Cahier, City, Country, Logement


class CahierSerializer(ModelSerializer):
    logements = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cahier


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country


class CitySerializer(ModelSerializer):

    class Meta:
        model = City


class LogementSerializer(ModelSerializer):

    class Meta:
        model = Logement
