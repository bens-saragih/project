from django import forms
from baca.models import artikel

class formartikel(forms.ModelForm):
	class Meta:
		model = artikel
		fields = [
			'penulis',
			'judul',
			'body',
			'category',

		]