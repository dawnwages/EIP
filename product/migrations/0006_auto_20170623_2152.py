# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-24 01:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170623_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Tag',
            new_name='Tags',
        ),
    ]
