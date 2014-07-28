from django.db import models

# Create your models here.
class Wower(models.Model):
	qq = models.CharField(max_length=50)
	truename = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	arrivings = models.SmallIntegerField()

	def __unicode__(self):
		return "%s, %s, %d" %(self.qq, self.truename, self.arrivings)
		

class Arriving(models.Model):
	qq = models.CharField(max_length=50)
	date = models.DateField()
	status = models.SmallIntegerField()

	def __unicode__(self):
		return "%s, %s, %d" %(self.qq, self.date, self.status)