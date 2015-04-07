from uuid import uuid4
import datetime

from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


class Course(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField('Name', max_length=100)
    )
    api_slug = models.SlugField('API Slug', max_length=20, unique=True, primary_key=True,
                                db_index=True, help_text='Only visible in the API.')

    def __str__(self):
        return self.name



class Module(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField('Name', max_length=100)
    )
    uuid = models.UUIDField('UUID', default=uuid4, editable=False, db_index=True, primary_key=True)
    course = models.ForeignKey(Course, related_name='modules')
    unit_based = models.BooleanField('Unit Based', default=True)

    def __str__(self):
        return self.name


class Unit(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField('Name', max_length=100)
    )
    uuid = models.UUIDField('UUID', default=uuid4, editable=False, db_index=True, primary_key=True)
    release_date = models.DateTimeField('Release Date', null=True)
    icon = models.ImageField(upload_to='unit_icons', height_field=None,
                             width_field=None, max_length=250, null=True,
                             blank=True)

    def __str__(self):
        return self.name


class Challenge(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField('Name', max_length=100)
    )
    uuid = models.UUIDField('UUID', default=uuid4, editable=False, db_index=True, primary_key=True)
    endurance = models.BooleanField('Endurance', default=False)
    unit = models.ForeignKey(Unit, related_name='challenges', null=True, blank=True)

    def __str__(self):
        return self.name




# class TVSeries(TranslatableModel):
#     distributor = models.CharField(max_length=255)

#     translations = TranslatedFields(
#         title = models.CharField(max_length=100),
#         subtitle = models.CharField(max_length=255),
#         released = models.DateTimeField(),
#         meta={'unique_together': [('title', 'subtitle')]},
#     )
