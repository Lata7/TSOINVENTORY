# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:29:38 2022

@author: Kevin
"""
#29555272
#LATA

from datetime import datetime
from enum import Enum, IntEnum


class Action(IntEnum):
    Breakfast = 1
    Lunch = 2
    Dinner = 3
    Sleep = 4
    Gym = 5
    Class = 6
    Church = 7
    Television = 8
    River = 9

class Days(IntEnum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

class Agent: #agent class
    def __init__(self, initialstate):
       self.state = initialstate
       pass
    def sense_world(self, dt, sick):
    
        return self.state

    def perform_action(self, hour, day):

        #00:00 - 05:00
        # used %s for the weekday and hour, although the small s had to show abbreviated days
        if hour >= 0 and hour <= 5:           
            return   "Day is:%s and I was sleeping at %s:00" % (day,hour)
        
        #06:00
        if hour == 6:
            if day == "Saturday" or day == "Sunday" :
                return "Day is:%s and I was sleeping at %s:00" % (day, hour)
            else:
                return "Day is:%s I was having breakfast at %s:00" % (day, hour)
            
        #07:00
        if hour == 7:                          
            if day == "Monday" or day == "Wednesday" or day == "Friday":
                return "Day is:%s and I was at the gym at %s:00" % (day, hour)
            elif day == "Tuesday" or day == "Thursday":
                return "Day is:%s and I was in class at %s:00" % (day, hour)
            else:
                return "Day is:%s and I was sleeping at %s:00" % (day, hour)
         
        #08:00 - 12:00       
        if hour == 8:
            if day == "Saturday" or day == "Sunday":
                return "Day is:%s and I was sleeping at %s:00" % (day, hour)
        if hour == 9:
            if day =="Saturday" or day == "Sunday":
                return "Day is:%s I was having breakfast at %s:00" % (day, hour)
        if hour == 10:
            if day == "Saturday" :
                return "Day is:%s and I was at the river at %s:00" % (day, hour)
            elif  day == "Sunday":
                return "Day is:%s and I was in church at %s:00" % (day, hour)
        if hour == 11 or hour == 12:
            if day == "Saturday" or day == "Sunday":
                return "Day is:%s and I was at the river at %s:00" % (day, hour)
        if hour == 11 or hour == 12:
            if day != "Saturday" or day != "Sunday":
                return "Day is:%s and I was in class at %s:00" % (day, hour)

        #13:00
        if hour == 13:
            if day == "Saturday" or day == "Sunday":
                return "Day is:%s and I was at the river at %s:00" % (day, hour)
            else:
                 return "Day is:%s and I was on lunch at %s:00" % (day, hour)

        #14:00 - 16:00        
        if hour == 14:
            if day == "Saturday" or day == "Sunday":
                return "Day is:%s and I was on lunch at %s:00" % (day, hour)
        if hour == 15 or hour == 16:
            if day == "Saturday" or day == "Sunday":
                return "Day is:%s and I was at the river at %s:00" % (day, hour)
        if hour >=14 and hour <=16:
            if day != "Saturday" or day != "Sunday":
                return "Day is:%s and I was in class on at %s:00" % (day, hour)

        #17:00 - 18:00
        if hour == 17 or hour == 18:
            if day == "Saturday" or day == "Sunday":
                return "Day is:%s and I'm at the river at %s:00" % (day, hour)
            else:
                return "Day is:%s and I was watching television at %s:00" % (day, hour)

        #19:00
        if hour == 19:
            return "Day is:%s and I was having dinner at %s:00" % (day, hour)

        #20:00 - 21:00
        if hour == 20 or hour == 21:
            return "Day is:%s and I was watching television at %s:00" % (day, hour)

        #22:00 - 23:00
        if hour == 22 or hour == 23:
            return "Day is:%s and I was sleeping at %s:00" % (day, hour)
        