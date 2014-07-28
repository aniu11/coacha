from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext

# Create your views here.
def navigate(request):
	return render_to_response("index.html", RequestContext(request))


def aboutme(request):
	return render_to_response("aboutme.html", RequestContext(request))

