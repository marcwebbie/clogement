# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cahier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('budget', models.FloatField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('uuid', models.UUIDField(editable=False, db_index=True, default=uuid.uuid4)),
                ('quartier', models.CharField(blank=True, max_length=255, null=True)),
                ('code_postal', models.CharField(blank=True, max_length=255, null=True)),
                ('prix', models.FloatField()),
                ('garantie', models.FloatField(default=0)),
                ('caution', models.FloatField(default=0)),
                ('charges', models.FloatField(default=0)),
                ('surface', models.IntegerField()),
                ('etage', models.IntegerField()),
                ('num_pieces', models.IntegerField()),
                ('num_chambres', models.IntegerField()),
                ('ascenseur', models.IntegerField()),
                ('num_places_parking', models.IntegerField()),
                ('climatisation', models.BooleanField()),
                ('purificateur_deau', models.BooleanField()),
                ('gardien', models.BooleanField()),
                ('piscine', models.BooleanField()),
                ('playground', models.BooleanField()),
                ('gym', models.BooleanField()),
                ('spa', models.BooleanField()),
                ('espace_enfant', models.BooleanField()),
                ('espace_barbecue', models.BooleanField()),
                ('cahier', models.ForeignKey(to='cahiers.Cahier', related_name='logements')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Pays',
            },
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('pays', models.ForeignKey(to='cahiers.Pays')),
            ],
        ),
        migrations.AddField(
            model_name='logement',
            name='ville',
            field=models.ForeignKey(to='cahiers.Ville'),
        ),
    ]
