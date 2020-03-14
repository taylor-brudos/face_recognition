from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from django.conf.urls import url
from . import views

urlpatterns = [ 
	path('image_upload', views.image_upload), 
    url('detect', views.detect),
    url(r'^$', views.index),
] 

if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL, 
							document_root=settings.MEDIA_ROOT) 
