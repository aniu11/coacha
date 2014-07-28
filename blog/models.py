#coding=utf-8
from django.db import models

# Create your models here.
class Article(models.Model):
	author = models.CharField(max_length = 50)
	title = models.CharField(max_length = 50)
	content = models.TextField(max_length = 10000)
	readCount = models.SmallIntegerField()

	#关键词列表
	#采用空格分离，解析时split
	keywords = models.CharField(max_length = 100)

	#类别
	#1：程序类
	#2：随笔类
	category = models.SmallIntegerField()

	datetime = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return "%s" %(self.title)
