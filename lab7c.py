#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    return sec_to_time(time_to_sec(t1) + time_to_sec(t2))

def change_time(time, seconds):
    new = sec_to_time(time_to_sec(time) + seconds)
    time.hour, time.minute, time.second = new.hour, new.minute, new.second

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True
def time_to_sec(time):
    return time.hour*3600 + time.minute*60 + time.second

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds,60)
    t.hour, t.minute = divmod(minutes,60)
    return t
