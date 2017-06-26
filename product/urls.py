from django.conf.urls import include, url
from . import views
from product.views import UserDetailView

urlpatterns = [
    url(r'^sku_list/$', UserDetailView.as_view(), name='home_list'),
    url(r'^sku_detail/(?P<pk>\d+)/$', views.sku_detail, name='sku_detail'),
    url(r'^article_list/$', views.article_list, name='article_list'),
    url(r'^article_detail/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    ]