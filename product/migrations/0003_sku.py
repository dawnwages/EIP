# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-19 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_auto_20170519_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sku_Num', models.CharField(max_length=20)),
                ('Friendly_Name', models.CharField(max_length=200)),
                ('Country_Choice', models.CharField(choices=[('United States', 'US'), ('Canada', 'CA')], default='United States', max_length=15)),
                ('Status_Choices', models.CharField(choices=[('Live', 'Live'), ('Not Live', 'Not Live/Removed From Site'), ('Blocked', 'Blocked'), ('Temporarily Unavailable', 'Temporarily Unavailable')], default='Live', max_length=200)),
                ('SKU_Choices', models.CharField(choices=[('Made to Manufacture', 'Made to Manufacture'), ('Configurable to Order', 'Configurable to Order')], default='Made to Manufacture', max_length=200)),
                ('SKU_Link', models.TextField(default='NULL')),
                ('Price_Choice', models.CharField(choices=[('1', 'Above $3,000'), ('2', 'Between $1,000 - $2999.99'), ('3', 'Between $500 - $999.99'), ('4', 'Between $100 - $499.99')], default='3', max_length=15)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('live_date', models.DateTimeField(blank=True, null=True)),
                ('Sku_Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('color_choice', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='product.color')),
                ('display_choice', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='product.display')),
                ('hd_choice', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='product.hd')),
                ('memory_choice', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='product.memory')),
                ('os_choice', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='product.os')),
                ('processor_choice', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='product.processor')),
                ('ss_choice', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='product.ss')),
            ],
        ),
    ]
