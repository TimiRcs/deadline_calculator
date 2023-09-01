#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, sys
from datetime import date, timedelta
from dateutil.easter import easter

startd = input("Irja be a hatarozat idopontjat kotojelekkel elvalasztva: ")
startday = date.fromisoformat(startd)
  
def PlusDays():
    global endday
    endday = startday + timedelta(days=15)
    return endday


def WeekEnd():
    global endday
    what_d = date.isoweekday(endday)
    if what_d == 6:
        endday = endday + timedelta(days=2)
            
    elif what_d == 7:
        endday = endday + timedelta(days=1)
            
    return endday    


def Holidays():
    PlusDays()
    WeekEnd()
    JudicalVacation()
    
    this_year = startday.year
    easter_sunday = easter(this_year, 3)
    easter_mon = easter_sunday + timedelta(days=1)
    easter_sat = easter_sunday - timedelta(days=1)
    easter_fri = easter_sunday - timedelta(days=2)
    punkosd = easter_sunday + timedelta(days=50)

    global endday
    
    # március 15.
    if endday == date.fromisoformat(f"{this_year}-03-15"):
        endday = endday + timedelta(days=1)
                
    # munka ünnepe
    elif endday == date.fromisoformat(f"{this_year}-05-01"):
        endday = endday + timedelta(days=1)
                
    # október 23.
    elif endday == date.fromisoformat(f"{this_year}-10-23"):
        endday = endday + timedelta(days=1)
                
    # mindenszentek
    elif endday == date.fromisoformat(f"{this_year}-11-01"):
        endday = endday + timedelta(days=1)
                
    #húsvét
    elif endday == easter_sunday:
        endday = easter_sunday + timedelta(days=2)
                
    elif endday == easter_mon:
        endday = easter_sunday + timedelta(days=2)
                
    elif endday == easter_sat:
        endday = easter_sunday + timedelta(days=2)
                
    elif endday == easter_fri:
        endday = easter_sunday + timedelta(days=2)
                   
    #pünkösd
    elif endday == punkosd:
        endday = endday + timedelta(days=1)
        
    WeekEnd()
        
    return endday


def JudicalVacation():
    global endday
    this_year = startday.year
    next_year = (endday + timedelta(weeks=52)).year
    
    #nyári
    if endday.month == 7:
        days_left1 = endday.day - 14
        if days_left1 > 0:
            endday = date.fromisoformat(f"{this_year}-08-20") + timedelta(days=days_left1)
    
    #téli
    elif endday.month == 12:
        days_left2 = endday.day - 23
        if days_left2 > 0:
            endday = date.fromisoformat(f"{next_year}-01-01") + timedelta(days=days_left2)
    
    WeekEnd()
    
    return endday


def WriteDate():
    global endday
    Holidays()
    print(f"A hatarido vege {endday} napjan vegzodik")


WriteDate()