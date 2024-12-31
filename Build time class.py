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
        #print
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
    
    def __add__(self, other):
        #Add two objects together
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes + (seconds // 60)
        hours = self.hours + other.hours + (minutes // 60)

        return Time(hours%24, minutes%60, seconds%60)

    def __gt__(self, other):
        #greater than
        return (self.hours > other.hours) \
                or (self.hours == other.hours and self.minutes > other.minutes) \
                or (self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds)
    
    def __eq__(self, other):
        return (self.hours == other.hours)

time1 = Time(13, 1, 20)
time2 = Time(13, 2, 40)

print(time1)
print(time2)
# print(time1 + time2)
# print(time1 > time2)
print(time1 == time2)
        