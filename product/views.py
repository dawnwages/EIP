from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db import models
from .models import Article, Sku

#def sku_list(request, *args, **kwargs):
#    Skus = sku.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
#    return render(request, 'product/sku_list.html', {'Skus': Skus})
#class IndexView(ListView):
#	context_object_name = 'home_list'
#	template_name = 'product/sku_list.html'
#	queryset = sku.objects.all()
#
#	def get_context_data(self, **kwargs):
#		context = super(IndexView, self).get_context_data(**kwargs)
#		context['sites'] = article.objects.all()
#		return context

#ORIGINAL LIST THAT IS REFERENCED FROM DJANGO GIRLS
#def sku_list(request, *args, **kwargs):
 #   skus = Sku.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
 #   return render(request, 'product/sku_list.html', {'skus': skus})

def total_list(request):
    #portfolio = Sku.objects.select_related('article__article_num')
    portfolio = Sku.objects.select_related('article')
    #queryset = portfolio.article
    return render(request, 'product/sku_list.html', {'portfolio': portfolio})

def sku_detail(request, pk):
    sku = get_object_or_404(Sku, pk=pk)
    return render(request, 'product/sku_detail.html', {'sku': sku})


def article_list(request):
    articles = Article.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
    return render(request, 'product/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'product/article_detail.html', {'article': article})

