from django.db import models

class RawImage(models.Model): 
    name = models.CharField(max_length=50)
    raw_image_img = models.ImageField(upload_to='images/')
