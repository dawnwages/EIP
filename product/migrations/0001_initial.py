# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-27 15:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('ArticleList_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Article_Num', models.CharField(max_length=20)),
                ('Series_Name', models.CharField(max_length=200)),
                ('BrandSeg_Choice', models.CharField(choices=[('Consumer', 'Consumer'), ('Commercial', 'Commercial')], default='Consumer', max_length=200)),
                ('Device_Status', models.CharField(choices=[('Live', 'Live'), ('Coming Soon', 'Coming Soon'), ('End of Life', 'End of Life')], default='Live', max_length=200)),
                ('Device_Choice', models.CharField(choices=[('Laptops', 'Laptops'), ('Desktops', 'Desktops'), ('Desktops - AIO', 'Desktops All-In-Ones'), ('Accessories', 'Accessories'), ('Workstations', 'WorkStations'), ('Tablets', 'Tablets'), ('Smart Devices', 'Smart Devices'), ('Servers Storage and Networking', 'Servers, Storage and Networking')], default='Laptops', max_length=200)),
                ('TaskLink', models.TextField(blank=True)),
                ('HLink', models.TextField()),
                ('AssetLinks', models.TextField(blank=True)),
                ('Notes', models.TextField(blank=True)),
                ('Halo', models.BooleanField(default=False)),
                ('Touch', models.BooleanField(default=False)),
                ('Convertible', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('live_date', models.DateTimeField(blank=True, null=True)),
                ('launch_notes', models.TextField()),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Os',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
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
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('color_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Color')),
                ('display_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Display')),
                ('hd_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Hd')),
                ('memory_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Memory')),
                ('os_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Os')),
                ('processor_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Processor')),
            ],
        ),
        migrations.CreateModel(
            name='Ss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='sku',
            name='ss_choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Ss'),
        ),
        migrations.AddField(
            model_name='article',
            name='Brand_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Brand'),
        ),
        migrations.AddField(
            model_name='article',
            name='Tags',
            field=models.ManyToManyField(to='product.Tag'),
        ),
    ]
