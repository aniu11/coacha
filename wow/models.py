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

class Notice(models.Model):
	qq = models.CharField(max_length=50)
	content = models.CharField(max_length=200)
	datetime = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return "%s, %s, %s" %(self.qq, self.datetime, self.content)

class Comment(models.Model):
	name = models.CharField(max_length=50)
	content = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s, %s" %(self.qq, self.content)

		