# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('topics', '0015_auto_20151201_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarytopicpage',
            name='feed_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, help_text='This image will be used in listings and indexes across the site, if no feed image is added, the social image will be used.', blank=True, related_name='+', to='images.IETFImage'),
        ),
        migrations.AlterField(
            model_name='primarytopicpage',
            name='social_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, help_text="Image to appear alongside 'social text', particularly for sharing on social networks", blank=True, related_name='+', to='images.IETFImage'),
        ),
        migrations.AlterField(
            model_name='secondarytopicpage',
            name='feed_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, help_text='This image will be used in listings and indexes across the site, if no feed image is added, the social image will be used.', blank=True, related_name='+', to='images.IETFImage'),
        ),
        migrations.AlterField(
            model_name='secondarytopicpage',
            name='social_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, help_text="Image to appear alongside 'social text', particularly for sharing on social networks", blank=True, related_name='+', to='images.IETFImage'),
        ),
        migrations.AlterField(
            model_name='topicindexpage',
            name='feed_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, help_text='This image will be used in listings and indexes across the site, if no feed image is added, the social image will be used.', blank=True, related_name='+', to='images.IETFImage'),
        ),
        migrations.AlterField(
            model_name='topicindexpage',
            name='social_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, help_text="Image to appear alongside 'social text', particularly for sharing on social networks", blank=True, related_name='+', to='images.IETFImage'),
        ),
    ]
