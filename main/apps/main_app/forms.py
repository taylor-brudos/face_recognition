from django import forms 
from .models import *

class ImageUploadForm(forms.ModelForm): 

	class Meta: 
		model = RawImage
		fields = ['raw_image_img']
