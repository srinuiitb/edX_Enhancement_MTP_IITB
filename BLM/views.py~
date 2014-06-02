from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime 

def index(request):
	#return HttpResponse("This is the first View in this project")
	#all_students = Student.objects.all()
	#output = ' '.join([i.name for i in all_students])
	return HttpResponse("BLM Home Page")

def hello(request):
	return HttpResponse("Hello world!, This is testing")

def homepage(request):
	return HttpResponse("This is ROOT homepage")

def time_now(request):
	time = datetime.datetime.now()
	html = "<html><body> TIME IS NOW %s : " % time
	return HttpResponse(html)

def hours_ahead(request, offset):	
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	time = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>After %s hour(s), it will be %s.</body></html>" % (offset, time)
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)
