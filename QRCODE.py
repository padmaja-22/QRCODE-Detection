import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('QR code.png')
cap = cv2.VideoCapture(0)   #capture from camera at location 0
#setting the width and height
cap.set(3,640)
cap.set(4,480)

while True:
    success,img=cap.read()
    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        points = np.array([barcode.polygon],np.int32)
        points = points.reshape((-1,1,2))
        cv2.polylines(img,[points],True,(139,0,0),5)
        points2 = barcode.rect
        cv2.putText(img,myData,(points2[0],points2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(139,0,0),2)
    cv2.imshow('Result',img)
    cv2.waitKey(1)
