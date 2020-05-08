import time
from datetime import datetime

class time_utils:
    def __init__(self):
        self.comp={
            'year':int(datetime.now().strftime("%Y")),
            'month':int(datetime.now().strftime("%m")),
            'day':int(datetime.now().strftime("%d")),
            'hour':int(datetime.now().strftime("%H")),
            'minute':int(datetime.now().strftime("%M")),
            'second':int(datetime.now().strftime("%S")),
        }
        self.dt=datetime(self.comp['year'],self.comp['month'],self.comp['day'],self.comp['hour'],self.comp['minute'],self.comp['second'])

    def get_current_time(self):
        return self.dt

    def datetime_to_int(self,dt):
        return int(dt.strftime("%Y%m%d%H%M%S"))

    def time_algo(self,num):
        # decompose
        year=self.comp['year']
        month=self.comp['month']
        day=self.comp['day']
        hour=self.comp['hour']
        minute=self.comp['minute']
        second=self.comp['second']

        # algorithm
        hour=hour+num
        if hour>=24: # check hours
            hour=hour-24
            day=day+1
        if month>0 and month<=12: # check month and day
            if month==1 and month==3 and month==5 and month==7 and month==8 and month==10 and month==12:
                if day>31:
                    day=0
                    month=month+1
            elif month==2:
                if day>29:
                    day=0
                    month=month+1
            elif month==4 and month==6 and month==9 and month==11:
                day=0
                month=month+1
        else: # check year
            year=year+1


        # restructure
        self.str_next_dt = datetime(year,month,day,hour,minute,second)
        self.int_next_dt = self.datetime_to_int(self.str_next_dt)

        return self.str_next_dt, self.int_next_dt

    def get_time(self):
        # current time (int)
        current_time_int=self.datetime_to_int(self.dt)
        # next available time (int)
        next_time_int=self.int_next_dt
        # current time (str)
        current_time_str=self.dt
        # next available time (str)
        next_time_str=self.str_next_dt
        return current_time_int, current_time_str, next_time_str

