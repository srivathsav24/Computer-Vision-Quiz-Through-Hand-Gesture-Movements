import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time
import sys


def fun(ent):
    print(ent)
    cap=cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    detector=HandDetector(detectionCon=0.8)


    class MCQ():
        def __init__(self,data):
            self.question = data[0]
            self.choice1 = data[1]
            self.choice2 = data[2]
            self.choice3 = data[3]
            self.choice4 = data[4]
            self.answer = int(data[5])
            
            self.userAns = None


        def update(self,cursor,bboxs):
            for x,bbox in enumerate(bboxs):
                x1,y1,x2,y2=bbox
                if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                    self.userAns=x+1
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),cv2.FILLED)


            

    #import csv data 
    pathcsv="Mcqs.csv"
    with open(pathcsv,newline='\n') as f:
        reader = csv.reader(f)
        dataAll=list(reader)[1:]
    # print(data)
    # print(len(data))

    #create object for each mcq
    mcqlist=[]
    for q in dataAll:
        mcqlist.append(MCQ(q))
    # print(len(mcqlist))

    qno=0
    qtotal=len(dataAll)


    while True:
        success,img=cap.read()
        img=cv2.flip(img,1)
        hands,img=detector.findHands(img,flipType=False)
        img, _ =cvzone.putTextRect(img,f'   CANDIDATE NAME : {ent}',[200,100],2,2,offset=16,border=2,colorB=(0,255,0),colorR=(0,0,0))
        img, bbox5 =cvzone.putTextRect(img,"EXIT",[800,100],2,2,offset=16,border=2,colorB=(0,255,0),colorR=(0,0,0))
                
        def exi(cursor,bbox):
            x1,y1,x2,y2=bbox
            if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),cv2.FILLED)
                sys.exit()

        if hands:
            lmList=hands[0]['lmList']
            cursor=lmList[4]
            length,info,img=detector.findDistance(lmList[4],lmList[16],img)
            if length<60:
                exi(cursor,bbox5)

        if qno<qtotal:

            mcq=mcqlist[qno]
            img,bbox=cvzone.putTextRect(img,mcq.question,[200,200],2,2,offset=20,border=2,colorB=(255,255,255),colorR=(0,0,255))
            img,bbox1=cvzone.putTextRect(img,mcq.choice1,[200,300],2,2,offset=20,border=2,colorB=(255,255,255),colorR=(250,105,20))
            img,bbox2=cvzone.putTextRect(img,mcq.choice2,[200,400],2,2,offset=20,border=2,colorB=(255,255,255),colorR=(250,105,20))
            img,bbox3=cvzone.putTextRect(img,mcq.choice3,[200,500],2,2,offset=20,border=2,colorB=(255,255,255),colorR=(250,105,20))
            img,bbox4=cvzone.putTextRect(img,mcq.choice4,[200,600],2,2,offset=20,border=2,colorB=(255,255,255),colorR=(250,105,20))

            if hands:
                lmList=hands[0]['lmList']
                cursor=lmList[8]
                length,info,img=detector.findDistance(lmList[8],lmList[12],img)
                if length<60:
                    mcq.update(cursor,[bbox1,bbox2,bbox3,bbox4])
                    # print(mcq.userAns)
                    if mcq.userAns is not None:
                        time.sleep(1)
                        qno+=1
        else:
            score=0
            for mcq in mcqlist:
                if mcq.answer==mcq.userAns:
                    score+=1
            score=round((score/qtotal)*100,2)
            img, _ =cvzone.putTextRect(img," QUIZ IS COMPLETED ",[250,300],2,2,offset=50,border=2,colorB=(255,255,255),colorR=(100,100,0))
            img, _ =cvzone.putTextRect(img,f'YOUR SCORE : {score}%',[800,300],2,2,offset=50,border=2,colorB=(255,255,255),colorR=(100,100,0),colorT=(0,0,255))

            # print(score)
        barValue=150+(950//qtotal)*qno
        cv2.rectangle(img,(150,700),(barValue,650),(0,255,0),cv2.FILLED)
        cv2.rectangle(img,(150,700),(barValue,650),(255,0,255),5)
        img, _ =cvzone.putTextRect(img,f'{round((qno/qtotal)*100)}%',[1130,700],2,2,offset=16,border=2,colorB=(255,255,255),colorR=(100,100,0))



        cv2.imshow("img",img)
        cv2.waitKey(1)