#!/usr/bin/python3
import sys
import json
from utils import db_argparser
from utils.db_utils import *
from utils.authentication import auth

db=db()
parser=db_argparser()

admin=False

# Token is for authorizing your identity
# Ask admin if you dont have one
ACCESS_TOKEN="TOKEN" # <- Switch User


def header(string):
    num=len(string)+2
    print('+','-'*num,'+')
    print('| ',string+' ','|')
    print('+','-'*num,'+')

def authorized():
    global admin
    authorized, is_admin = auth().identity_check(ACCESS_TOKEN)
    if is_admin == True:
        admin=True
        return True
    if authorized:
        return True

def main():
    # Determine if there is a user input
    if len(sys.argv)>1:

        if authorized(): # authorization

            # Admin special rights
            if parser.get_args().init: # create a new user
                if admin:
                    auth().init()
                else:
                    print('-> Authorization failed, your current user account does not have the right ...')
                    sys.exit(1)
            if parser.get_args().get_users:
                if admin:
                    if parser.get_args().all: # get the list of all registered users
                        auth().get_config()
                    else:
                        username=parser.get_args().name # get info of a registered user
                        auth().get_user(username)
                else:
                    print('-> Authorization failed, your current user account does not have the right ...')
                    sys.exit(1)
        
            # User normal rights
            if parser.get_args().fetch: # read data from db
                if not parser.get_args().name:
                    db.get_data('db')
                else:
                    name=parser.get_args().name
                    db.get_data(name)
            if parser.get_args().remove: # remove data from db
                db_name=parser.get_args().name
                if parser.get_args().all: # remove all
                    db.clear_db(db_name)
                else:
                    val=parser.get_args().id
                    db.remove_data('_id',val)
            if parser.get_args().update: # updata data
                id=parser.get_args().id
                name=parser.get_args().name
                db.update_data(id,'name',name)  
        else:
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__=='__main__':
    main()
