from django.shortcuts import render
from .models import artikel
# Create your views here.

def index(request):
	semua_artikel = artikel.objects.all()
	categories = artikel.objects.values('category').distinct()
	context = {
		'judul':'Baca Artikel',
		'heading':'Ayo Baca Artikel ....',
		'semua_artikel':semua_artikel,
		'Categories':categories
	}
	return render (request,'baca/index.html',context)


def detailartikel(request,sluginput):
	semua_artikel  = artikel.objects.get(slug=sluginput)
	context = {
		'judul':'Isi Artikel',
		'heading':'Isi Artikel',
		'semua_artikel':semua_artikel
	}
	return render(request,'baca/detail.html',context)


def categoryartikel(request,categoryinput):
	semua_artikel = artikel.objects.filter(category=categoryinput)
	categories = artikel.objects.values('category').distinct()
	context = {
		'judul':'Category',
		'heading':'Category..',
		'semua_artikel':semua_artikel,
		'Categories':categories
	}
	return render(request,'baca/category.html',context)