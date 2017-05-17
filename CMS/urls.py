from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^post/new/$', views.simple_upload, name='post_new'),
	]