# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 23:10
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeptName', models.TextField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avitar', models.FileField(blank=True, null=True, upload_to='media/')),
                ('pictures', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/profile_photos/'), upload_to=b'')),
                ('FirstName', models.TextField(blank=True, default='', max_length=50)),
                ('FullName', models.TextField(blank=True, default='', max_length=50)),
                ('bio', models.TextField(blank=True, default='', max_length=500)),
                ('location', models.CharField(blank=True, default='', max_length=30)),
                ('Dept_Choices', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Departments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
