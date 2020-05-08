import json
import ast
from datetime import datetime
import qrcode
import os
from tinydb import TinyDB, Query
from .timer import time_utils

DB=TinyDB('./db/db.json')
Check_in_DB=TinyDB('./db/check_in_db.json')
User=Query()
Check_in=Query()

check_List={
    "name_List":[],
    "record":[]
}

# time=time_utils()

class db():
    def __init__(self):
        self.db=DB
        self.check_in_db=Check_in_DB
        self.query=User

    def header(self,string):
        num=len(string)+2
        print('+','-'*num,'+')
        print('| ',string+' ','|')
        print('+','-'*num,'+')

    def get_data(self,db):
        if(db=='db'):
            db=self.db
        else:
            db=self.check_in_db
        if len(db)==0:
            self.header('db is empty!')
        else:
            self.header('all data fetched!')
            for item in db:
                print('-> ',item)

    def clear_db(self,db):
        if db=='db':
            self.db.truncate()
            # delete QR Code data
            for item in self.db.all():
                id=item['_id']
                os.remove('./data/{}.png'.format(id))
        else:
            self.check_in_db.truncate()
        self.header('db is cleared!')

    def remove_data(self,field,val):
        # delete QR Code data
        item=self.db.search(self.query[field]==val)[0]
        os.remove('./data/{}.png'.format(item['_id']))
        # remove from db
        self.db.remove(self.query[field]==val)
        self.header('data removed!')

    def add_data(self,data):
        data=ast.literal_eval(data) # convert to dict
        self.db.insert(data) # add to db
        self.header('new data added!')
        print('-> ',data)

    def search_data(self,field,val):
        self.header('data found!')
        for item in (self.db.search(self.query[field]==val)):
            print('-> ',item)

    def update_data(self,id,field,value):
        self.header('data updated!')
        self.db.update({field:value}, self.query._id==id)
        print('-> ',self.db.search(self.query._id==id))
        data=self.db.search(self.query._id==id)[0]
        # delete original qr_code
        os.remove('./data/{}.png'.format(data['_id']))
        # generate a new qr_code
        qr=qrcode.QRCode(
            version=1,
            box_size=15,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('./data/{}.png'.format(data['_id']))
        self.header('new QR Code saved!')

    def get_dataList(self):
        myDataList=[]
        for item in self.db.all():
            myDataList.append(item)
        return myDataList

    def check_in(self,identity,checked,num):
        # get time
        time=time_utils() # new time instance
        time.time_algo(num)
        current_time_int, current_time_str, next_time_str = time.get_time()
        # print(current_time_int, current_time_str, next_time_str)

        global check_List

        if checked==1: 
            status='checked'
            if identity['name'] in check_List['name_List']:
                for record in check_List['record']:
                    if identity == record['identity']:
                        if current_time_int >= record['next_time_int']: # check if already checked in
                            # add record to db
                            data={
                                'check_in_status':status,
                                'check_in_time':str(current_time_str),
                                'next_available_check_in_time':str(next_time_str),
                                'identity':identity
                            }
                            next_time_int=time.datetime_to_int(next_time_str)
                            
                            # add check_in data to db
                            self.check_in_db.insert(data)
                            self.header('a person checked in!')
                            print('-> ',data)
                            
                            # delete record from check_list and then add the new record
                            check_List['record'].remove(record)
                            check_List['record'].append({'identity':identity,'next_time_int':next_time_int,'added':True})
                            print(check_List)

                            # reset check_in_time time

            elif identity['name'] not in check_List['name_List']:
                # add record to db
                data={
                    'check_in_status':status,
                    'check_in_time':str(current_time_str),
                    'next_available_check_in_time':str(next_time_str),
                    'identity':identity
                }
                next_time_int=time.datetime_to_int(next_time_str)
                
                # add check_in data to db
                self.check_in_db.insert(data)
                self.header('a person checked in!')
                print('-> ',data)
                # store record in check_list
                check_List['name_List'].append(identity['name'])
                check_List['record'].append({'identity':identity,'next_time_int':next_time_int,'added':True})
                # print(check_List)
                
                # reset check_in_time
                current_time_str=current_time_str

