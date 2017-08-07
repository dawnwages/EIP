from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db import models
from .models import Article, Sku

<<<<<<< HEAD
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

class UserDetailView(DetailView):
	subseries = article
	
	def get_context_data(self, **kwargs):
		#Calling the get_context_data parent
		parts = sku.objects.filter(Sku_Article = context['sites']).order_by('-live_date')

		tags = [ subserie.tag.all() for subserie in subseries]

		total_portfolio = self.get_total(parts) #Calling the function that return the total sku list/ total portfolio/ all of the parts
		context['portfolio'] = zip(parts, tags, total_portfolio)

		return context

	def get_total(self, parts):
		#return the total portfolio that a subseries has
		return[ parts.objects.filter(part__id=part.id).annotat(num_answers=Count('part')).count() for part in parts]
=======
#ORIGINAL LIST THAT IS REFERENCED FROM DJANGO GIRLS
#def sku_list(request, *args, **kwargs):
 #   skus = Sku.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
 #   return render(request, 'product/sku_list.html', {'skus': skus})

def total_list(request):
	#portfolio = Sku.objects.select_related('article__article_num')
	portfolio = Sku.objects.select_related('article')
	#queryset = portfolio.article
   	return render(request, 'product/sku_list.html', {'portfolio': portfolio})
>>>>>>> Finally freaking fixed the models and Foreign Key and template tag reltionship on sku_list.html

def sku_detail(request, pk):
    sku = get_object_or_404(Sku, pk=pk)
    return render(request, 'product/sku_detail.html', {'sku': sku})


def article_list(request):
    articles = Article.objects.filter(live_date__lte=timezone.now()).order_by('-live_date')
    return render(request, 'product/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'product/article_detail.html', {'article': article})

