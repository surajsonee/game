from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registration(models.Model):
	title        = models.CharField(max_length=200)
	newstext     = models.CharField(max_length=200)
	newsvideourl = models.CharField(max_length=200)
	fburl        = models.CharField(max_length=200)
	twiterurl    = models.CharField(max_length=200)
	youtubeurl   = models.CharField(max_length=200)

	def __unicode__(self):

	#function returns unicode representaion of a task
		return self.title

