import cv2
import numpy as np
from pyzbar.pyzbar import decode
import json
from .db_utils import db
from ast import literal_eval

font=cv2.FONT_HERSHEY_SIMPLEX

db=db()
myDataList=db.get_dataList()

class opencv():
    def decode(self,myData):
        data=literal_eval(myData)
        return data

    def authorization(self,myData):
        check=False
        # decode myData
        data = self.decode(myData)
        if data in myDataList:
            check=True
            color=(0,255,0)
            msg='Authorized!'
            db.check_in(data,1,3)
            # Do something else
        else:
            color=(0,0,255)
            msg='Unauthorized!'
        return check,color,msg

    def draw_bbox(self,img,qrcode,myData):
        check,color,msg = self.authorization(myData) # authorization
        cv2.putText(img,"Detecting",(10,45),font,0.5,(0,255,0),2)
        pts_rect=qrcode.rect
        # if authorized draw green box, else draw red box
        cv2.putText(img,msg,(pts_rect[0],pts_rect[1]-5),font,0.6,color,2)
        pts=np.array([qrcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,color,5)

    def fps_display(self,img,timer):
        fps=cv2.getTickFrequency()/(cv2.getTickCount()-timer)
        cv2.putText(img,"FPS: "+str(int(fps)),(10,20),font,0.5,(255,255,255),2)
