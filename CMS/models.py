from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
		author = models.ForeignKey('auth.User')
		title = models.CharField(max_length=200)
		email = models.CharField(max_length=200)
		url = models.CharField(max_length=255, blank=True) #RFC 3986 states there is no limit, but the hostname is limited to 255 characters because of DNS limitations.
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
		asset = models.FileField(upload_to='post_assets/%Y/%m/')
		created_date = models.DateTimeField(
			default=timezone.now)
		published_date = models.DateTimeField(
			blank=True, null=True)

		def publish(self):
			self.published_date = timezone.now()
			self.save()

		def __str__(self):
			return self.title

