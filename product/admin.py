from __future__ import unicode_literals

from django.contrib import admin
from .models import Processor, Os, Memory, Hd, Display, Ss, Color, Brand, Article, Sku, Tag 
#Make sure all of the models in models.py that you want included in your administrative site are included


# Register your models here.
admin.site.register(Processor)
admin.site.register(Os)
admin.site.register(Memory)
admin.site.register(Hd)
admin.site.register(Display)
admin.site.register(Ss)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Article)
admin.site.register(Sku)
admin.site.register(Tag)