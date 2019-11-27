from django.shortcuts import render,redirect
from baca.models import artikel
from .forms import formartikel
# Create your views here.

def index(request):
	semua_artikel = artikel.objects.all()
	context = {
		'penulis'
		'judul':'All Artikel',
		'heading':'All Artikel',
		'semua_artikel':semua_artikel,
	}
	return render(request,'edit/index.html',context)


def create(request):
	form_artikel = formartikel(request.POST or None)

	if request.method =='POST':
		if form_artikel.is_valid():
			form_artikel.save()
		return redirect('edit:index')
	context = {
		'judul':'Create',
		'heading':'Buat Artikel',
		'form_artikel':form_artikel
	}
	return render(request,'edit/create.html',context)

def delete(request,delete_id):
	artikel.objects.filter(id=delete_id).delete()
	return redirect('edit:index')

def update(request,update_id):
	update_artikel = artikel.objects.get(id=update_id)
	data = {
		'judul':update_artikel.judul,
		'body':update_artikel.body,
	}
	form_artikel = formartikel(request.POST or None,initial=data, instance=update_artikel)
	if request.method == 'POST':
		if form_artikel.is_valid():
			form_artikel.save()
		return redirect('edit:index')

	context = {
		'judul':'Update',
		'heading':'Update Artikel',
		'form_artikel':form_artikel
	}
	return render(request,'edit/create.html',context)
