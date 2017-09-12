# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save

#from mezzanine.core.fields import FileField
from django.dispatch import receiver

ps = FileSystemStorage(location='/media/profile_photos/')


class Departments(models.Model):
	DeptName = models.TextField(max_length=50, blank=True)
	def publish(self):
		self.live_date = timezone.now()
		self.save()
	def __str__(self):
		return self.DeptName


models.FileField(upload_to='media/', blank=True, null=True)

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
	avitar = models.FileField(upload_to='media/', blank=True, null=True)
	#avitar = models.FileField(verbose_name=_("Profile Picture"),
	#							upload_to=upload_to("main.Profile.avitar", "profiles"),
	#							format="Image", max_length=255, null=True, blank=True)
	pictures = models.ImageField(storage=ps, null=True, blank=True)
	FirstName = models.TextField(max_length=50, blank=True, default='')
	FullName = models.TextField(max_length=50, blank=True, default='')
	bio = models.TextField(max_length=500, blank=True, default='')
	location = models.CharField(max_length=30, blank=True, default='')
	#Model Type
	Dept_Choices = models.ForeignKey('profiles.Departments', null=True, default='')
	def publish(self):
		self.live_date = timezone.now()
		self.save()

	class Meta:
		verbose_name_plural = "User Profiles"

	def __str__(self):
		return self.user.username

def create_user_profile(sender, **kwargs):
	user = kwargs["instance"]
	if kwargs["created"]:
		user_profile = Profile(user=user)
		user_profile.save()
post_save.connect(create_user_profile, sender=User)