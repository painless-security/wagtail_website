# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-19 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0028_remove_snippits_primarytopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondarytopic',
            name='slug',
            field=models.CharField(max_length=511, blank=True),
        ),
    ]
