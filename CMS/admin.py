# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Link

admin.site.register(Post)
admin.site.register(Link)

# Register your models here.
