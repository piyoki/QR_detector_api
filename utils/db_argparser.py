import argparse

class db_argparser():
    def __init__(self):
        self.parser=argparse.ArgumentParser(description='Database Operations')
        self.parser.add_argument('-d','--fetch',help='fetech all data in the database',action='store_true')
        self.parser.add_argument('-r','--remove',help='remove data with id',action='store_true')
        self.parser.add_argument('-u','--update',help='update data with id',action='store_true')
        self.parser.add_argument('--all','--all',help='all',action='store_true')
        self.parser.add_argument('--init','--init',help='create a new user',action='store_true')
        self.parser.add_argument('--get_users','--get_user',help='check info of a registed user',action='store_true')
        self.parser.add_argument('--name','--name',help='specify name',type=str)
        self.parser.add_argument('--id','--id',help='specify id',type=str)
        self.parser.add_argument('--output','--output',help='output filename',type=str)
    def get_args(self):
        return self.parser.parse_args()
    def print_help(self):
        self.parser.print_help()