from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from timeline_web.models import Rankdata
from datetime import *
import urllib2
import json

# Create your views here.

def home(request):
	if 'birthday' in request.session:
		birthday = request.session['birthday']
		bstr = str(birthday)
		cal = bstr.split("/")
		renderlist = []
		for i in reversed(range(2010, date.today().year + 1)):
			qw = date(int(i),int(cal[0]),int(cal[1])).isocalendar()[1]
			try:
				result = Rankdata.objects.get(year=i,week=qw)
				result.yy = str(result.year)[2:4]
				result.share_thumb = result.youtube.replace("https://www.youtube.com/embed/","https://img.youtube.com/vi/")+"/0.jpg"
				renderlist.append(result)
			except:
				pass
		return render_to_response('../templates/timeline.html',{'token':'token','name':request.session['name'],'birthday':birthday,'renderlist':renderlist})
	else:
		return render_to_response('../templates/home.html')

def share(request):
        if request.method == 'GET':
                if 'birthday' in request.GET and 'name' in request.GET:
                        birthday = request.GET['birthday']
                	bstr = str(birthday)
                	cal = bstr.split("/")
                        renderlist = []
                        for i in reversed(range(2010, date.today().year + 1)):
                        	qw = date(int(i),int(cal[0]),int(cal[1])).isocalendar()[1]
                        	try:
                        		result = Rankdata.objects.get(year=i,week=qw)
                        		result.yy = str(result.year)[2:4]
                        		renderlist.append(result)
                        	except:
                        		pass
                        if 'access_token' in request.session:
                                return render_to_response('../templates/timeline_share.html',{'token':'token','name':request.GET['name'],'birthday':birthday,'renderlist':renderlist})
                        else:
                                return render_to_response('../templates/timeline_share.html',{'name':request.GET['name'],'birthday':birthday,'renderlist':renderlist})        
                else:
                        return HttpResponseRedirect('/')
        else:
                return HttpResponseRedirect('/')

def login(request):
	if request.method == 'GET':
		if 'access_token' in request.GET:
			token = request.GET['access_token']
			graph = urllib2.urlopen('https://graph.facebook.com/me?locale=ko_KR&access_token='+token)
			if graph.getcode() == 200:
				data = json.load(graph)
				if 'birthday' in data:
					request.session['access_token'] = token
					request.session['name'] = data['name']
					cal = str(data['birthday']).split("/")
					request.session['birthday'] = cal[0] + "/" + cal[1]
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/permission')
			else:
				return HttpResponseRedirect('/error')
		else:
			return HttpResponseRedirect('/error')
	else:
		return HttpResponseRedirect('/error')

def logout(request):
	for sesskey in request.session.keys():
		del request.session[sesskey]
	return HttpResponseRedirect('/')

def privacy(request):
	return render_to_response('../templates/privacy.htm')

def permission(request):
	return render_to_response('../templates/permission.html')
