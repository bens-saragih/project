from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.core.exceptions import ValidationError

#import file validator
from edit.validatorsn import validate_author
from edit.validatorsn import validate_body

class artikel(models.Model):
	judul = models.CharField(max_length=20)
	penulis = models.CharField(max_length=20,validators = [validate_author])
	list_category = (
		('blog','blog'),
		('berita','berita'),
		('jurnal','jurnal'),
		)
	category = models.CharField(max_length=20,choices=list_category,default='blog')
	body = models.TextField(validators=[validate_body])
	ditulis = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(blank=True,editable=False)

	def save(self):#agar secara otomatis akan tersimpan,tanpa perlu di isi
		self.slug = slugify(self.judul)# yang akan tersimpan sebagai slug ada judul
		super(artikel, self).save()

	def __str__(self):
		return "{}.{}".format(self.id,self.judul)