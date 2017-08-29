from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
		author = models.ForeignKey('auth.User')
		title = models.CharField(max_length=200)
		email = models.CharField(max_length=200)
		url = models.URLField(max_length=255, blank=True) #RFC 3986 states there is no limit, but the hostname is limited to 255 characters because of DNS limitations.
		Update_1 = '/static/img/update_1.jpg'
		Update_2 = '/static/img/update_2.jpg'
		Update_3 = '/static/img/update_3.jpg'
		Update_4 = '/static/img/update_4.jpg'
		Update_5 = '/static/img/update_5.jpg'
		Update_Types = (
			(Update_1, 'Promotions'),
			(Update_2, 'Special Projects'),
			(Update_3, 'Campaigns'),
			(Update_4, 'Holidays'),
			(Update_5, 'Tests')
			)
		Update_Choices = models.CharField(
			max_length=200,
			choices=Update_Types,
			default=Update_2,
			)
		text = models.TextField(blank=True)
		asset = models.FileField(upload_to='post_assets/%Y/%m/',blank=True)
		created_date = models.DateTimeField(
			default=timezone.now)
		published_date = models.DateTimeField(
			blank=True, null=True)

		def publish(self):
			self.published_date = timezone.now()
			self.save()

		def __str__(self):
			return self.title


class Link(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	url = models.URLField(max_length=200)
	description = models.CharField(max_length=2000)
	link_1 = '/static/icon/icons8-Filing Cabinet-50.png'
	link_2 = '/static/icon/icons8-Support Filled-50.png'
	link_3 = '/static/icon/icons8-Binoculars Filled-50.png'
	link_4 = '/static/icon/icons8-Whois-50.png'
	link_5 = '/static/icon/icons8-Key Filled-50.png'
	link_types = (
		(link_1, 'Internal Ops'),
		(link_2, 'Tools'),
		(link_3, 'Info Resource'),
		(link_4, 'Lenovo link'),
		(link_5, 'Calendar')
		)
	link_choices = models.CharField(
		max_length=200,
		choices=link_types,
		default=link_2,
		)

	created_date = models.DateTimeField(
		default=timezone.now)
	
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title