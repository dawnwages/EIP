from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^links/$', views.link_list, name='link_list'),
	url(r'^calendar/$', views.calendar, name='calendar'),
	]