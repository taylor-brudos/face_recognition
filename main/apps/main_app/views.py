from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .forms import *
import numpy as np
import urllib
import json
import cv2
import os


FACE_DETECTOR_PATH = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(base_path=os.path.abspath(os.path.dirname(__file__)))

def index(request):
    form = ImageUploadForm() 
    return render(request, "main_app/index.html", {'form' : form})

def image_upload(request):
    ImageUploadForm(request.POST, request.FILES).save()
    return redirect('/image_display')

def image_display(request): 
	return HttpResponse('successfully uploaded') 

@csrf_exempt
def detect(request):
	data = {"success": False}
	if request.method == "POST":
		if request.FILES.get("image", None) is not None:
			image = _grab_image(stream=request.FILES["image"])
		else:
			url = request.POST.get("url", None)
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)
			image = _grab_image(url=url)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
		rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5,
			minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
		rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]
		data.update({"num_faces": len(rects), "faces": rects, "success": True})
	return JsonResponse(data)

def _grab_image(path=None, stream=None, url=None):
	if path is not None:
		image = cv2.imread(path)
	else:	
		if url is not None:
			resp = urllib.request.urlopen(url)
			data = resp.read()
		elif stream is not None:
			data = stream.read()
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image
