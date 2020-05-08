import cv2
import qrcode
import json
from pyzbar.pyzbar import decode
import numpy as np
from .qr_argparser import qr_argparser
from .db_utils import db
import uuid

db = db()

class qr_code():
    def __init__(self):
        self.qr=qrcode.QRCode(
            version=1,
            box_size=15,
            border=5
        )

    def header(self, string):
        num=len(string)+2
        print('+','-'*num,'+')
        print('| ',string+' ','|')
        print('+','-'*num,'+')

    def data_constructor(self):
        parser=qr_argparser()
        data={
            '_id':str(uuid.uuid1()),
            'name':parser.get_args().name
        }
        return data
    def create(self):
        data=self.data_constructor()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill='black', back_color='white')
        img.save('./data/{}.png'.format(data['_id']))
        self.header('QR Code created!')
        print('-> ','data: {}'.format(data))
        # add data to db
        data=json.dumps(data) #json str
        db.add_data(data)
    def decode(self,input_file):
        img = cv2.imread(input_file)
        code=decode(img)
        self.header('Decoding QR Code data ...')
        for barcode in decode(img):
            data = barcode.data.decode('utf-8')
            print('-> ',data)
