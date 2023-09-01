#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from datetime import date, timedelta
from dateutil.easter import easter

class AppealCalculator:
    
    def __init__(self, startd: str, startday = date.today()):
        self.startd = startd
        self.startday = startday
        try:
            self.startday = date.fromisoformat(startd)
        except:
            print("Rosszul adta meg a datumot, a hatarido a mai naptol van szamolva. Probalja ujra pl: 2023-01-01")
    
    def PlusDays(self):
        self.endday = self.startday + timedelta(days=15)
        return self.endday

    def WeekEnd(self):
        what_d = date.isoweekday(self.endday)
        if what_d == 6:
            self.endday = self.endday + timedelta(days=2)
                
        elif what_d == 7:
            self.endday = self.endday + timedelta(days=1)
                
        return self.endday    

    def Holidays(self):
        self.PlusDays()
        self.WeekEnd()
        self.JudicalVacation()
        
        this_year = self.startday.year
        easter_sunday = easter(this_year, 3)
        easter_mon = easter_sunday + timedelta(days=1)
        easter_sat = easter_sunday - timedelta(days=1)
        easter_fri = easter_sunday - timedelta(days=2)
        punkosd = easter_sunday + timedelta(days=50)
        
        # március 15.
        if self.endday == date.fromisoformat(f"{this_year}-03-15"):
            self.endday = self.endday + timedelta(days=1)
                    
        # munka ünnepe
        elif self.endday == date.fromisoformat(f"{this_year}-05-01"):
            self.endday = self.endday + timedelta(days=1)
                    
        # október 23.
        elif self.endday == date.fromisoformat(f"{this_year}-10-23"):
            self.endday = self.endday + timedelta(days=1)
                    
        # mindenszentek
        elif self.endday == date.fromisoformat(f"{this_year}-11-01"):
            self.endday = self.endday + timedelta(days=1)
                    
        #húsvét
        elif self.endday == easter_sunday:
            self.endday = easter_sunday + timedelta(days=2)
                    
        elif self.endday == easter_mon:
            self.endday = easter_sunday + timedelta(days=2)
                    
        elif self.endday == easter_sat:
            self.endday = easter_sunday + timedelta(days=2)
                    
        elif self.endday == easter_fri:
            self.endday = easter_sunday + timedelta(days=2)
                    
        #pünkösd
        elif self.endday == punkosd:
            self.endday = self.endday + timedelta(days=1)
            
        self.WeekEnd()
            
        return self.endday

    def JudicalVacation(self):
        this_year = self.startday.year
        next_year = (self.endday + timedelta(weeks=52)).year
        
        #nyári
        if self.endday.month == 7:
            days_left1 = self.endday.day - 14
            if days_left1 > 0:
                self.endday = date.fromisoformat(f"{this_year}-08-20") + timedelta(days=days_left1)
        
        #téli
        elif self.endday.month == 12:
            days_left2 = self.endday.day - 23
            if days_left2 > 0:
                self.endday = date.fromisoformat(f"{next_year}-01-01") + timedelta(days=days_left2)
        
        self.WeekEnd()
        
        return self.endday

    def WriteDate(self):
        self.Holidays()
        print(f"A hatarido vege {self.endday} napjan vegzodik")
