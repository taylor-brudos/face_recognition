import requests
import cv2

url = "http://localhost:8000/detect/"

image = cv2.imread("pictures/taylor.png")
payload = {"image": open("pictures/taylor.png", "rb")}
r = requests.post(url, files=payload).json()
# print("pictures/taylor.png: {}".format(r))
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
cv2.imshow("pictures/taylor.png", image)
cv2.waitKey(0)
