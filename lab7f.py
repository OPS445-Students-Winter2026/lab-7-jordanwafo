class Time:
    def __init__(self,hour=12,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        return self.hour*3600 + self.minute*60 + self.second

    def sum_times(self, t2):
        return sec_to_time(self.time_to_sec() + t2.time_to_sec())

    def change_time(self, seconds):
        nt = sec_to_time(self.time_to_sec() + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True
    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
    def __add__(self, t2):
        return self.sum_times(t2)

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds,60)
    t.hour, t.minute = divmod(minutes,60)
    return t
