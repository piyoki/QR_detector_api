import argparse

class qr_argparser():
    def __init__(self):
        self.parser=argparse.ArgumentParser(description='specify QR Code parameters')
        self.parser.add_argument('-n','--name',help='specify name',type=str)
        self.parser.add_argument('--input','--input',help='specify input file path',type=str)
        self.parser.add_argument('-d','--decode',help='decode code with id',action='store_true')
        self.parser.add_argument('-r','--run',help='run the app',action='store_true')
    def get_args(self):
        return self.parser.parse_args()
    def print_help(self):
        self.parser.print_help()