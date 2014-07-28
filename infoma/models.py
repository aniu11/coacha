from django.db import models

# Create your models here.

class Graduate(models.Model):
	qq = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	classNum = models.SmallIntegerField()
	address = models.CharField(max_length=200)
	tel = models.CharField(max_length=20)
	motto = models.CharField(max_length=500)

	def __unicode__(self):
		return self.name