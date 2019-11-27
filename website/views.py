from django.shortcuts import render

def index(request):
	context = {
		'judul':'Home | Project',
		'heading':'Selamat Datang di Project CRUD Sederhana'
	}
	return render(request,'index.html',context)