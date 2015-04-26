from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from cahiers.serializers import CahierSerializer, CountrySerializer, CitySerializer, LogementSerializer
from cahiers.models import Cahier, Country, City, Logement


class CahierViewSet(ViewSet):

    def list(self, request):
        queryset = Cahier.objects.all()
        serializer = CahierSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new Cahier
        ---
        serializer: cahiers.serializers.CahierSerializer
        """
        serializer = CahierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Cahier.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CahierSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Cahier.objects.get(pk=pk)
        except Cahier.DoesNotExist:
            return Response(status=404)
        serializer = CahierSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Cahier.objects.get(pk=pk)
        except Cahier.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CountryViewSet(ViewSet):

    def list(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new Country
        ---
        serializer: cahiers.serializers.CountrySerializer
        """
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CountrySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response(status=404)
        serializer = CountrySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CityViewSet(ViewSet):

    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new City
        ---
        serializer: cahiers.serializers.CitySerializer
        """
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=404)
        serializer = CitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LogementViewSet(ViewSet):

    def list(self, request):
        queryset = Logement.objects.all()
        serializer = LogementSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new Logement
        ---
        serializer: cahiers.serializers.LogementSerializer
        """
        serializer = LogementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Logement.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = LogementSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Logement.objects.get(pk=pk)
        except Logement.DoesNotExist:
            return Response(status=404)
        serializer = LogementSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Logement.objects.get(pk=pk)
        except Logement.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
