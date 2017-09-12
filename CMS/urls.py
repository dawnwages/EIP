from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
	# url(r'^admin/', admin.site.urls),
	url(r'^product/', include('product.urls', namespace='product')),
	url(r'^accounts/', include('profiles.urls', namespace='profiles')),


	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

	url(r'^links/$', views.link_list, name='link_list'),
	url(r'^calendar/$', views.calendar, name='calendar'),
	]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)