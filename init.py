#!/usr/bin/python3
import os
import subprocess
import shlex
import json
from utils import db_argparser
from utils.db_utils import *
from utils.authentication import auth

parser=db_argparser()

def main():

    cmd = 'mkdir ./config'
    path='/config'
    args=shlex.split(cmd)
    subprocess.call(args)
    cmd = 'mkdir ./data'
    args=shlex.split(cmd)
    subprocess.call(args)
    auth().set_path('./config')
    auth().init()

    print('->  config.json is saved to path: ',os.getcwd()+path)
    print('->  You may now log in as admin !')

if __name__=='__main__':
    main()