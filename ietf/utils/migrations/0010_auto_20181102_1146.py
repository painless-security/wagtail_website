# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-02 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0009_feedsettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedsettings',
            options={'verbose_name': 'Feeds'},
        ),
    ]
