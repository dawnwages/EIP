from django.conf.urls import include, url
from . import views
from product.views import UserDetailView


urlpatterns = [
<<<<<<< HEAD
    url(r'^sku_list/$', UserDetailView.as_view(), name='home_list'),
=======
    url(r'^sku_list/$', views.total_list, name='home_list'),
>>>>>>> Finally freaking fixed the models and Foreign Key and template tag reltionship on sku_list.html
    url(r'^sku_detail/(?P<pk>\d+)/$', views.sku_detail, name='sku_detail'),
    url(r'^article_list/$', views.article_list, name='article_list'),
    url(r'^article_detail/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    ]