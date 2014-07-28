#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
import time
from datetime import *
from infoma.models import Graduate
# Create your views here.

def auth(request):
	if("authorized" in request.COOKIES):
		return HttpResponseRedirect("/infoma/self")
	else:
		return render_to_response("auth.html", RequestContext(request))

def self(request):
	if("authorized" in request.COOKIES):
		return render_to_response("self.html", RequestContext(request))
	else:
		return auth(request)

def store_information(request):
	#从request中获取表单变量
	qq = request.REQUEST.get("qq")
	name = request.REQUEST.get("name")
	address = request.REQUEST.get("address")
	tel = request.REQUEST.get("tel")
	classNum = request.REQUEST.get("classNum")
	motto = request.REQUEST.get("motto")

	#创建一个graduate
	person = Graduate(qq=qq, name=name, address=address, tel=tel, classNum=classNum, motto=motto)

	#检测QQ是否存在
	if Graduate.objects.filter(qq=qq).exists():
		#如存在，删除旧的信息
		Graduate.objects.get(qq=qq).delete()

	person.save()
	
	#定位至结果页面
	return HttpResponseRedirect("result")

def result(request):

	if("authorized" in request.COOKIES):
		#获取数据集中结果
		result = get_result()

		#生成上下文
		c = Context({'result': result})

		#渲染模板
		return render_to_response('result.html', c, RequestContext(request))
	else:
		return auth(request)

def check(request):
	ans = request.REQUEST.get("ans")
	if ans == u"郑松山":
		response = HttpResponseRedirect('/infoma/result')
		response.set_cookie("authorized", "bingo", 3600000)
		return response
	else:
		return render_to_response("error.html", RequestContext(request))



def get_result():
	result = []

	#取得所有数据
	people = Graduate.objects.all()
	for person in people:
		#将单个数据加入结果集
		result.append(person)
	return result
