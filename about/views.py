from django.shortcuts import render

# Create your views here.
def index(request):
	context={
		'judul':'About',
		'heading':'Halama About'
	}
	return render(request,'about/index.html',context)