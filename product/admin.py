from __future__ import unicode_literals

from django.contrib import admin
from .models import processor, os, memory, hd, display, ss, color, Brand, article, sku, Tag 

# Register your models here.
admin.site.register(processor)
admin.site.register(os)
admin.site.register(memory)
admin.site.register(hd)
admin.site.register(display)
admin.site.register(ss)
admin.site.register(color)
admin.site.register(Brand)
admin.site.register(article)
admin.site.register(sku)
admin.site.register(Tag)