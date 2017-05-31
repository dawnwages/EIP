from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class processor(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class os(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class memory(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class hd(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class display(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class ss(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class color(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Brand(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class article(models.Model):
		author = models.ForeignKey('auth.User')
		ArticleList_ID = models.AutoField(primary_key=True)
		Article_Num = models.CharField(max_length=20,)
		Series_Name = models.CharField(max_length=200)
		#BrandSegment
		CON = 'Consumer'
		COM = 'Commercial'
		Brand_Type = (
			(CON, 'Consumer'),
			(COM, 'Commercial'),
			) 
		BrandSeg_Choice = models.CharField(
			max_length=200,
			choices=Brand_Type,
			default= CON,
			)
		#Brand
		Brand_Type = models.ForeignKey('product.brand')
		#Device Type
		Live = 'Live'
		CS = 'Coming Soon'
		EOL = 'End of Life'
		Status_Type = (
			(Live, 'Live'), 
			(CS, 'Coming Soon'),
			(EOL, 'End of Life'), 
			)
		Device_Status = models.CharField(
			max_length=200,
			choices=Status_Type,
			default= Live,
			)
		#Device Type
		LT = 'Laptops'
		DT = 'Desktops'
		DTA = 'Desktops - AIO'
		ACC = 'Accessories'
		WS = 'Workstations'
		TB = 'Tablets'
		SD = 'Smart Devices'
		SSN = 'Servers Storage and Networking'
		Device_Type = (
			(LT, 'Laptops'), 
			(DT, 'Desktops'),
			(DTA, 'Desktops All-In-Ones'),
			(ACC, 'Accessories'),
			(WS, 'WorkStations'),
			(TB, 'Tablets'),
			(SD, 'Smart Devices'),
			(SSN, 'Servers, Storage and Networking') 
			)
		Device_Choice = models.CharField(
			max_length=200,
			choices=Device_Type,
			default= LT,
			)
		TaskLink = models.TextField(blank=True)
		HLink = models.TextField()
		AssetLinks = models.TextField(blank=True)
		Notes = models.TextField(blank=True)
		Halo = models.BooleanField(default=False)
		Touch = models.BooleanField(default=False)
		Convertible = models.BooleanField(default=False)
		#Dates
		created_date = models.DateTimeField(
			default=timezone.now)
		live_date = models.DateTimeField(
			blank=True, null=True)
		launch_notes = models.TextField()
		def publish(self):
			self.live_date = timezone.now()
			self.save()
		def __str__(self):
			return self.Article_Num

class sku(models.Model):
		author = models.ForeignKey('auth.User')
		Sku_Num = models.CharField(max_length=20)
		Sku_Article = models.ForeignKey('product.article')
		Friendly_Name = models.CharField(max_length=200)
		#Country
		US = 'United States'
		CA = 'Canada'
		Country_Type = (
			(US, 'US'),
			(CA, 'CA'),
		)
		Country_Choice = models.CharField(
			max_length=15,
			choices=Country_Type,
			default=US,
			)
		#SKU STATUS
		Live = 'Live'
		NotLive = 'Not Live'
		BLOCKED = 'Blocked'
		TEMPUNAV = 'Temporarily Unavailable'
		Status_Type = (
			(Live, 'Live'),
			(NotLive, 'Not Live/Removed From Site'),
			(BLOCKED, 'Blocked'),
			(TEMPUNAV, 'Temporarily Unavailable'),
			)
		Status_Choices = models.CharField(
			max_length=200,
			choices=Status_Type,
			default=Live,
			)
		#Model Type
		MTM = 'Made to Manufacture'
		CTO = 'Configurable to Order'
		SKU_Type = (
			(MTM, 'Made to Manufacture'), 
			(CTO, 'Configurable to Order')
			)
		SKU_Choices = models.CharField(
			max_length=200,
			choices=SKU_Type,
			default= MTM,
			)
		SKU_Link = models.TextField(default='NULL')
		processor_choice = models.ForeignKey('product.processor', default='NULL',)
		os_choice = models.ForeignKey('product.os', default='NULL',)
		memory_choice = models.ForeignKey('product.memory', default='NULL')
		hd_choice = models.ForeignKey('product.hd', default='NULL')
		display_choice = models.ForeignKey('product.display', default='NULL')
		ss_choice = models.ForeignKey('product.ss', default='NULL')
		color_choice = models.ForeignKey('product.color', default='NULL')
		TierOne = '1'
		TierTwo = '2'
		TierThree = '3'
		TierFour = '4'
		#Price Choices
		Price_Tier = (
			(TierOne, 'Above $3,000'),
			(TierTwo, 'Between $1,000 - $2999.99'),
			(TierThree, 'Between $500 - $999.99'),
			(TierFour, 'Between $100 - $499.99'),
			)
		Price_Choice = models.CharField(
			max_length=15,
			choices=Price_Tier,
			default=TierThree,
			)
		#Dates
		created_date = models.DateTimeField(
			default=timezone.now)
		live_date = models.DateTimeField(
			blank=True, null=True)
		def publish(self):
			self.created_date = timezone.now()
			self.save()
		def __str__(self):
			return self.Sku_Num