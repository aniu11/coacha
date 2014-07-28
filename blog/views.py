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
	p = Paginator(blog_list, 1)

	page = request.GET.get("page", 1)
	try:
		blogs = p.page(page)
	except EmptyPage:
		blogs =  p.page(paginator.num_pages)

	c = Context({'blogs': blogs})
	
	return render_to_response("index_blog.html", c, RequestContext(request))

def passage(request):
	id = request.REQUEST.get("id")
	if not Article.objects.filter(id = id).exists():
		return HttpResponse("该文章不存在！")
	else:
		blog = Article.objects.get(id = id)
		#对博文进行预处理
		blog = process(blog)
		c = Context({'blog': blog})
		return render_to_response("passage.html", c, RequestContext(request))

#获取博文数据的工具方法
#处理markdown的步骤在其中完成
def get_blogs():
	ans = []
	blogs = Article.objects.all()

	for blog in blogs:
		#对博文进行预处理
		blog = process(blog)
		ans.append(blog)
	return ans

def process(blog):
	#分离keywords
	blog.keywords = blog.keywords.split(' ')
	#处理markdown标记语言，转换为html标记
	blog.content = markdown(blog.content)
	return blog