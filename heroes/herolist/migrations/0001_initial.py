# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('generic_name', models.CharField(max_length=15, unique=True)),
                ('display_name', models.CharField(max_length=45)),
                ('hero_type', models.CharField(db_index=True, max_length=3, choices=[('INT', 'Intelligence'), ('AGI', 'Agility'), ('STR', 'Strength')])),
                ('short_desc', models.CharField(null=True, blank=True, max_length=255)),
                ('image_filename', models.CharField(max_length=255, default='default.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='Synergy',
            fields=[
                ('hero', models.OneToOneField(serialize=False, to='herolist.Hero', primary_key=True, related_name='rel_hero')),
                ('counters', models.ManyToManyField(related_name='rel_hero_foes', to='herolist.Hero')),
                ('friends', models.ManyToManyField(related_name='rel_hero_friends', to='herolist.Hero')),
            ],
        ),
    ]
