# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-14 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0003_auto_20170828_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='asset',
            field=models.FileField(default='/static/img/No_image_available.svg', upload_to='post_assets/%Y/%m/'),
        ),
    ]
