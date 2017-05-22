from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import article, sku

def sku_list(request):
    Skus = sku.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
    return render(request, 'product/sku_list.html', {'Skus': Skus})

def sku_detail(request, pk):
    Sku = get_object_or_404(sku, pk=pk)
    return render(request, 'product/sku_detail.html', {'Sku': Sku})


def article_list(request):
    Articles = article.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
    return render(request, 'product/article_list.html', {'Articles': Articles})

def article_detail(request, pk):
    Article = get_object_or_404(article, pk=pk)
    return render(request, 'product/article_detail.html', {'Article': Article})

