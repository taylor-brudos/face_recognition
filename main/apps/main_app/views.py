from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .forms import *
import numpy as np
import urllib
import json
import cv2
import os

def index(request):
    form = ImageUploadForm() 
    return render(request, "main_app/index.html", {'form': form})

def image_upload(request):
    form = ImageUploadForm(request.POST, request.FILES)
    form.save()
    image_path = './media/images/' + str(request.FILES['raw_image_img'])
    directory='./media/images'
    detect(image_path)
    return redirect('/')

def detect(image_path):
    FACE_DETECTOR_PATH = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(base_path=os.path.abspath(os.path.dirname(__file__)))
    image = cv2.imread(image_path)
    detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
    rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]
    for (startX, startY, endX, endY) in rects:
	    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    cv2.imshow('Face Detected', image)
    cv2.waitKey(0)
