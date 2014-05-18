from django.http import HttpResponse

def index(request):
	#return HttpResponse("This is the first View in this project")
	all_students = Student.objects.all()
	output = ' '.join([i.name for i in all_students])
	return HttpResponse(output)
