#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
import time
from datetime import *
from wow.models import Arriving
from wow.models import Wower

#第一次登录时触发的方法，返回验证页面
def first_in(request):
	#如果用户已经登录过，那么直接重定向至结果页面
	if "login_wow" in request.COOKIES:
		return HttpResponseRedirect('/wow/result')
	return render_to_response("auth_wow.html", RequestContext(request))

#处理post验证表单的方法，如成功跳转到结果页
#需要注意的是，当用户请求/wow/auth时，实际用于渲染页面的是first_in方法
#auth方法不用于渲染页面，而用于用户提交表单后进行逻辑处理
def auth(request):
	qq = request.REQUEST.get("qq")

	if Wower.objects.filter(qq = qq).exists():
		name = Wower.objects.get(qq = qq).truename
		response = HttpResponseRedirect('/wow/result')
		response.set_cookie("qq", qq, 3600000)
		response.set_cookie("login_wow", "1", 3600000)
		return response
	else:
		return first_in(request)

#显示结果的方法，获取参数并传递
def result(request):
	if not "login_wow" in request.COOKIES:
		#如未登录，返回登录界面
		return first_in(request)
	else:
		#获取状态列表
		status = get_status()
		#获取qq和name的映射关系
		names = get_names()
		#获取最近一周日期信息
		dates = get_dates()
		#获取当前登录名称
		qq = request.COOKIES["qq"]
		username = Wower.objects.get(qq = qq).truename

		c = Context({'status': status, 'names': names, 'dates': dates, 'username': username})
		return render_to_response("result_wow.html", c, RequestContext(request))

#该方法用于更新arriving数据
def update(request):
	checklist = request.REQUEST.getlist("checklist")
	qqnum = request.COOKIES["qq"]
	today = date.today()

	for i in range(0, 7):
		shifted_date = today + timedelta(i)
		if Arriving.objects.filter(qq = qqnum, date = shifted_date).exists():
			p = Arriving.objects.get(qq = qqnum, date = shifted_date)
			if str(i) in checklist:
				p.status = 1
			else:
				p.status = 0
			p.save()
		else:
			p = Arriving(qq = qqnum, date = shifted_date, status = 2)
			if str(i) in checklist:
				p.status = 1
			else:
				p.status = 0
			p.save()

	return HttpResponseRedirect("/wow/result")


#登出，清空cookie中login_wow字段。但是不影响存储的qq字段d
#如需更换用户登录，再次登录时会设置login_wow字段，并将qq字段重置
def logout(request):
	if not "login_wow" in request.COOKIES:
		#如未登录，返回登录界面
		return first_in(request)
	else:
		response = HttpResponseRedirect('/wow')
		response.delete_cookie('login_wow')
		return response

#此方法是重构后增加的方法，用于建立qq到truename的映射
#在未找到很好的模板查询方法时，该方法暂未投入使用，直接采用truename作为键值
def get_names():
	#建立字典
	#key：qq -> value：truename
	ans = {}
	people = Wower.objects.all()
	for person in people:
		ans[person.qq] = person.truename
	return ans

#该方法是get_arrivings_array()的重构版本。使用qq作为键值，而不是truename
def get_status():
	ans = {}
	people = Wower.objects.all()
	curr_date = date.today()
	for person in people:
		#在status中，状态由如下规定：
		#0：确定不到
		#1：确定到
		#2：未确定
		#在此，status全被初始化成状态2，即未确定状态
		status_array = [2, 2, 2, 2, 2, 2, 2]
		for i in range (0, 7):
			if(Arriving.objects.filter(qq = person.qq, date = curr_date).exists()):
				status_array[i] = Arriving.objects.get(qq = person.qq, date = curr_date).status
			curr_date = curr_date + timedelta(1)
		ans[person.truename] = status_array
		#person.name即为qq字段，这里命名不规范，应该对数据库字段进行修改
		#由于未找到在模板中查询第二字典的有效方法，故采用truename作为键值的方式。这里要求truename无重名
		curr_date = date.today()
	return ans


#该方法已更新于2014/7/22，更改了方法名
def get_dates():
	date_array = []
	curr_date = date.today()
	curr_weekday = curr_date.weekday()
	for i in range(0, 7):
		date_item = {'id': i, 'day_in_week': curr_weekday, 'weekday_str': weekday_str(curr_weekday), 'date':  curr_date}
		date_array.append(date_item)
		curr_date = curr_date + timedelta(1)
		curr_weekday = curr_date.weekday()
	return date_array

#该方法将weekday数值和中文名建立一一映射
def weekday_str(weekday):
	day_to_str = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	return day_to_str[weekday]
