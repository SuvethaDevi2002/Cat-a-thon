import numpy as np
from pyzbar.pyzbar import decode
import cv2
entry_list=""
vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,740)
with open('Autho.txt', 'r') as file:
    auth_list = file.read().strip()
    print(auth_list)
while True:
  success, img = vid.read()
  for barcode in decode(img):
    text = barcode.data.decode('utf-8')
    text=str(text)
    if text not in auth_list:
      color=(0,0,255)
      displaytext = "Unauthorised Access"
    else:
      entry_list = text
      color=(0,255,0)
      displaytext = "Access Granted"

    polygon_Points = np.array([barcode.polygon], np.int32)
    polygon_Points=polygon_Points.reshape(-1,1,2)
    rect_Points= barcode.rect
    cv2.polylines(img,[polygon_Points],True,color, 3)
    cv2.putText(img, displaytext, (rect_Points[0],rect_Points[1]), cv2.FONT_HERSHEY_PLAIN, 0.9, color, 2)
  print(entry_list)
  cv2.imshow("Video", img)
  cv2.waitKey(1)

