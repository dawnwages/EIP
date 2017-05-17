from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/new/$', views.simple_upload, name='post_new'),
	]