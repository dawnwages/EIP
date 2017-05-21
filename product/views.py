from django.shortcuts import render
from django.utils import timezone
from .models import article, sku

def sku_list(request):
    skus = sku.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
    return render(request, 'product/sku_list.html', {'skus': skus})