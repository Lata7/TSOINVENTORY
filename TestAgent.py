# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:30:11 2022

@author: Kevin
"""
#29555272
#LATA

from Agent import Action,Days, Agent
from datetime import datetime
from enum import Enum, IntEnum




index = int(input("Enter day: "))

if (index >= 1 and index <= 7):    
  
    testAgent = Agent(Days(index).name)
    hr = input ("Enter time: ")

    d1 = datetime(year = 2020, month = 2, day = 25, hour = int(hr) , minute = 55, second = 59)
                    
    print(testAgent.perform_action(int(d1.strftime("%H")), testAgent.sense_world(d1, False)))
          
    
else:
    print("INVALID")