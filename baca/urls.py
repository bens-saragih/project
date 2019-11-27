from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^post/(?P<sluginput>[\w-]+)/$',views.detailartikel,name='detail'),
	url(r'^category/(?P<categoryinput>[\w-]+)/$',views.categoryartikel,name='category')
]