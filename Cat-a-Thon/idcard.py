import cv2
import numpy as np
from pyzbar.pyzbar import decode
import datetime
Auth_data=""
e = datetime.datetime.now()

#print ("Current date and time = %s" % e)
d = "%s/%s/%s" % (e.day, e.month, e.year)

t = "%s:%s:%s" % (e.hour, e.minute, e.second)
#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('Autho.txt') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            Auth_data = myData
            myOutput = 'Authorized'
            myColor = (0,255,0)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)
        import csv

        header = ['Id number', 'Date', 'Time']
        data = [Auth_data, d,t]



       # writer.writerow(header)
        with open('entries.csv', 'a', newline='',encoding='UTF8') as f:
            writer = csv.writer(f)
            # write the header
            #writer.writerow(header)

            # write the data
            writer.writerow(data)
            break
        import pandas as pd
        file = pd.read_csv("entries.csv")
        file.to_csv("ids.csv",header=header,index=False)


    cv2.imshow('Result',img)
    cv2.waitKey(1)
