import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time
import  sys
def exi(cursor,bbox):
    x1,y1,x2,y2=bbox
    if x1<cursor[0]<x2 and y1<cursor[1]<y2:
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),cv2.FILLED)
        sys.exit()
        
            
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector=HandDetector(detectionCon=0.8)
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)
    # img, _ =cvzone.putTextRect(img,f'   CANDIDATE NAME : {ent}',[200,100],2,2,offset=16,border=2,colorB=(0,255,0),colorR=(0,0,0))
    img, bbox5 =cvzone.putTextRect(img,"EXIT",[800,100],2,2,offset=16,border=2,colorB=(0,255,0),colorR=(0,0,0))
    if hands:
        lmList=hands[0]['lmList']
        cursor=lmList[4]
        length,info,img=detector.findDistance(lmList[4],lmList[16],img)
        if length<60:
            exi(cursor,bbox5)

    cv2.imshow("img",img)
    cv2.waitKey(1)