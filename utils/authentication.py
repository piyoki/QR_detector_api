from .timer import time_utils
import sys
import json
import secrets
import string
import os
import getpass 

# default path
directoryPath='./config'

time=time_utils()

class auth():
    def header(self,string):
        num=len(string)+2
        print('+','-'*num,'+')
        print('| ',string+' ','|')
        print('+','-'*num,'+')
        
    def token_generator(self):
        token = secrets.token_urlsafe(20)
        return token

    def set_path(self,path):
        global directoryPath
        directoryPath=path
        print('-> config.json is set to save in:', directoryPath)

    def init(self):
        print('-> New user registration ...')
        username = input('-> Enter username: ')
        password = getpass.getpass(prompt='-> Enter password: ')
        print('-> Confirm your input: {}'.format({'username': username, 'password': password}))
        if input('-> Continue? [y/n] ') == 'y':
            # create a new user
            token=self.token_generator()
            user={
                'account_create_time':str(time.get_current_time()),
                'type':'user',
                'user_name':username,
                'password':password,
                'access_token':token
            }
            # create config.json (first time login)
            if os.listdir(directoryPath)==[]: 
                user['type']='admin'
                data={'user_list':[user]}
                self.header('config file created!')
            else:
                # read config.json
                with open('{}/config.json'.format(directoryPath),'r') as json_file:
                    data=json.load(json_file)
                    data['user_list'].append(user)

            # overite config.json
            with open('{}/config.json'.format(directoryPath),'w') as json_file:
                json.dump(data,json_file)

            self.header('new user added!')
            print('-> ',user)
            print('->  Please save your access token: <', user['access_token'],'> !')
        
        else:
            print('-> Quitting...')
            sys.exit(1)  

    def get_config(self):
        self.header("all registered users' data fetched!")
        # read config.json
        with open('{}/config.json'.format(directoryPath)) as json_file:
            data=json.load(json_file)
        for item in data['user_list']:
            print('-> ',item)

    def get_user(self,name):
        self.header('user identity data fetched!')
        with open('{}/config.json'.format(directoryPath)) as json_file:
            data=json.load(json_file)
        for item in data['user_list']:
            if name==item['user_name']:
                print('-> ',item)
    
    def identity_check(self,token):
        auth=False
        admin=False
        # read config.json
        with open('{}/config.json'.format(directoryPath)) as json_file:
            data=json.load(json_file)
        # read parameters from console
        self.header('User Authentication')

        username = input("-> Enter username: ")

        user_list=[]
        for record in data['user_list']:
            user_list.append(record['user_name'])

        if username in user_list:
            password = getpass.getpass(prompt='-> Enter password: ')
            for record in data['user_list']:
                if username == record['user_name']:
                    if password == record['password']:
                        if token == record['access_token']:
                            if record['type']=='admin':
                                print('-> (Admin) Login succesfully ...!!!')
                                self.header('Current User: '+username+' (Admin)')
                                admin=True
                            else:
                                print('-> Login successfully ...!!!')
                                self.header('Current User: '+username)
                            
                            auth=True                                
                        else:
                            print('-> Authentication failed, access token mismatched ...') 
                    else:
                        print('-> Authentication failed, please enter the correct password ...')
        else: 
            print('-> User does not exist !')
        
        return auth, admin