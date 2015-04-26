from django.conf import settings

from hashids import Hashids
from rest_framework import serializers


class HashidsField(serializers.Field):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('help_text', 'Hash id field')
        salt = kwargs.pop('salt', settings.HASHIDS_SALT)
        min_length = kwargs.pop('min_length', settings.HASHIDS_MIN_LENGTH)
        self.hashids = Hashids(salt=salt, min_length=min_length)
        super().__init__(*args, **kwargs)

    def to_representation(self, obj):
        return self.hashids.encode(obj)

    def to_internal_value(self, value):
        return self.hashids.decode(value)


class HashidsRelatedField(HashidsField):

    def __init__(self, queryset, *args, **kwargs):
        self.queryset = queryset
        self.many = kwargs.get('many', 'False')
        super().__init__(*args, **kwargs)

    def to_representation(self, obj):
        if self.many:
            return [super(HashidsRelatedField, self).to_representation(elem.pk)
                    for elem in self.queryset]
        else:
            return super().to_representation(obj.pk)

    def to_internal_value(self, value):
        value = super().to_internal_value(value)
        return self.queryset.get(pk=value)
