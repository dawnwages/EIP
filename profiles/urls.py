from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$', views.profile_page, name='profile_page'),
	url(r'^accounts/update/$', views.edit_user, name='account_update'),
]

