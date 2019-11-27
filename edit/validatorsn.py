from django.core.exceptions import ValidationError

def validate_author(value):
	judul_input = value
	if judul_input == "sariando":
		message = "maaf, tidak bisa posting"
		raise ValidationError(message)
		
def validate_body(value):
	body_input = value
	if body_input == "klik":
		message = "perkataan tersebut di larang di gunakan"
		raise ValidationError(message)