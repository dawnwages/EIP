from __future__ import unicode_literals

from django.contrib import admin
<<<<<<< HEAD
from .models import processor, os, memory, hd, display, ss, color, Brand, article, sku, Tag 
=======
from .models import Processor, Os, Memory, Hd, Display, Ss, Color, Brand, Article, Sku, Tag 
#Make sure all of the models in models.py that you want included in your administrative site are included

>>>>>>> Finally freaking fixed the models and Foreign Key and template tag reltionship on sku_list.html

# Register your models here.
admin.site.register(Processor)
admin.site.register(Os)
admin.site.register(Memory)
admin.site.register(Hd)
admin.site.register(Display)
admin.site.register(Ss)
admin.site.register(Color)
admin.site.register(Brand)
<<<<<<< HEAD
admin.site.register(article)
admin.site.register(sku)
=======
admin.site.register(Article)
admin.site.register(Sku)
>>>>>>> Finally freaking fixed the models and Foreign Key and template tag reltionship on sku_list.html
admin.site.register(Tag)