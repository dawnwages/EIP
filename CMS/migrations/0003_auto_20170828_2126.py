# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0002_auto_20170828_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='link',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
