from django.db import models

class RawImage(models.Model): 
    raw_image_img = models.ImageField(upload_to='images/', verbose_name="Selected Image")
