import traceback
from django.shortcuts import render
from django.http import *
from django.template import RequestContext
from socialapp.models  import Registration
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from socialapp.models import *

# Create your views here.
def home(request):
	news = Registration.objects.all()
	newsdetail = {
		"newsinfo" : news
	}
	print newsdetail
	return render_to_response('index.html',
	newsdetail, context_instance=RequestContext(request))

def news(request):
    """
    showing news page
    """
    return render_to_response('news.html')

@csrf_exempt
def save_news(request):
	"""
	save news in db
	"""
	try:
		title         = request.POST.get('title','Kunal')
		newstext      = request.POST.get('newstext','This is dummy text to show you')
		newsvideourl  = request.POST.get('newsvideourl','http://www.youtube.com/TusdxsxjQ1g/')
		fburl         = request.POST.get('fburl','http://www.facebook.com/')
		twiterurl     = request.POST.get('twiterurl','http://www.twitter.com/')
		youtubeurl    = request.POST.get('youtubeurl','http://www.youtube.com/')

		registration = Registration(title=title, newstext=newstext, newsvideourl=newsvideourl, fburl=fburl, twiterurl=twiterurl, youtubeurl=youtubeurl)
		registration.save()
	except:
		traceback.print_exc()
		return HttpResponse(" Failed To Save Project !")
	return HttpResponseRedirect('/', {'request':request})

#def news_detail(request):
	#news = Registration.objects.all()
	#newsdetail = {
	#	"newsinfo" : news
	#}
	#print newsdetail
	#return render_to_response('newsDetail.html',
	#newsdetail, context_instance=RequestContext(request))

def details(request, news_id):
	"""
	show details
	"""
	new = Registration.objects.get(id=news_id)	
	news = Registration.objects.all()
	newsdetail = {
		"newsinfo" : news
	}
	print newsdetail
	return render_to_response('newsDetail.html',
	newsdetail, context_instance=RequestContext(request))
