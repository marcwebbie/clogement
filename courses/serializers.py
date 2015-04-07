from rest_framework import serializers
from hvad.contrib.restframework import TranslatableModelSerializer

from .models import Challenge, Course, Unit


class CourseSerializer(TranslatableModelSerializer):
    class Meta:
        model = Course


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
