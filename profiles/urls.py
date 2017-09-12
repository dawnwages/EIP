from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^/profile/$', views.profile_page, name='profile_page'),
	url(r'^/update/$', views.edit_user, name='account_update'),
]

