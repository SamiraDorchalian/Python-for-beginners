import os

os.system('cls')

class Time:
    def __init__(self, hours, minutes, seconds):
        if hours >= 24:
            raise ValueError('Hours number should be less than 23.')
        if minutes >= 60:
            raise ValueError('Minutes number should be less than 60.')
        if seconds >= 60:
            raise ValueError('Second number should be less than 60.')
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

time1 = Time(17, 5, 42)
time2 = Time(14, 20, 35)

print(time1)
print(time2)
        