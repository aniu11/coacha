#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from models import *
from markdown import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
	#将文章列表等装入blog_list
	blog_list = get_blogs()
	#加入分页系统，一页显示三篇博文
	p = Paginator(blog_list, 3)

	page = request.GET.get("page", 1)
	try:
		blogs = p.page(page)
	except EmptyPage:
		blogs =  p.page(p.num_pages)

	c = Context({'blogs': blogs})
	
	return render_to_response("index_blog.html", c, RequestContext(request))

def passage(request):
	id = request.REQUEST.get("id")
	if not Article.objects.filter(id = id).exists():
		return render_to_response("error.html", RequestContext(request))
	else:
		blog = Article.objects.get(id = id)
		#对博文进行预处理
		blog = process(blog)
		c = Context({'blog': blog})
		return render_to_response("passage.html", c, RequestContext(request))

def content(request):
	category = request.REQUEST.get("category")


	blog_list = get_blogs(category)
	p = Paginator(blog_list, 10)

	page = request.GET.get("page", 1)
	try:
		blogs = p.page(page)
	except EmptyPage:
		blogs = p.page(p.num_pages)

	c = Context({'blogs': blogs, 'category': category})

	return render_to_response("content.html", c, RequestContext(request))

#获取博文数据的工具方法
#处理markdown的步骤在其中完成
#默认category = 0，即无过滤条件
def get_blogs(category = '0'):
	ans = []
	blogs = Article.objects.all()

	for blog in blogs:
		if category == '0' or str(blog.category) == category:	
			#对博文进行预处理
			blog = process(blog)
			ans.append(blog)
	#排序
	ans.sort(cmp = blog_cmp)
	#倒序
	ans.reverse()
	return ans

def process(blog):
	#分离keywords
	blog.keywords = blog.keywords.split(' ')
	#处理markdown标记语言，转换为html标记
	blog.content = markdown(blog.content)
	return blog

#blog的排序依据，作为参数传入
def blog_cmp(a, b):
	return cmp( a.datetime, b.datetime)