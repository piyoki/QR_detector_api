#!/usr/bin/python3
import cv2
import sys
import json
from pyzbar.pyzbar import decode
from utils import qr_argparser, qr_code, opencv

qr=qr_code()
parser=qr_argparser()
app=opencv()

def header(string):
    num=len(string)+2
    print('+','-'*num,'+')
    print('| ',string+' ','|')
    print('+','-'*num,'+')

def run():
    cap = cv2.VideoCapture(0)
    # Resize frame
    cap.set(3,640)
    cap.set(4,480)

    header('QR Code Detector running ...')

    while True:
        timer=cv2.getTickCount()
        success, img=cap.read()
        for qrcode in decode(img):
            myData = qrcode.data.decode('utf-8') #decode to str
            # print(myData)
            app.draw_bbox(img,qrcode,myData) # add bounding box

        app.fps_display(img,timer) # display fps
        cv2.imshow('QR_code Dector',img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    # Determine if there is a user input
    if len(sys.argv)>1:
        # Check certain types of argument
        if parser.get_args().name:
            qr.create()
        if parser.get_args().decode:
            input_file=parser.get_args().input
            qr.decode(input_file)
        if parser.get_args().run:  
            # Run the detection api
            run()
    else:
        parser.print_help()
        sys.exit(1)

if __name__=='__main__':
    main()