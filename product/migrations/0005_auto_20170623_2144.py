# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-24 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_article_device_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Tag',
            field=models.ManyToManyField(to='product.Tag'),
        ),
    ]
