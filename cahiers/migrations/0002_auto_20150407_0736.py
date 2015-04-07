# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cahiers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logement',
            old_name='purificateur_deau',
            new_name='purificateur_eau',
        ),
        migrations.RemoveField(
            model_name='logement',
            name='id',
        ),
        migrations.AddField(
            model_name='logement',
            name='balcon',
            field=models.BooleanField(default=datetime.datetime(2015, 4, 7, 5, 35, 47, 168770, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logement',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 4, 7, 5, 35, 56, 312859, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logement',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 4, 7, 5, 36, 12, 96352, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logement',
            name='jardin',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logement',
            name='phone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logement',
            name='phone2',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logement',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logement',
            name='etage',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='logement',
            name='num_chambres',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='logement',
            name='num_pieces',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='logement',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, serialize=False, primary_key=True),
        ),
    ]
