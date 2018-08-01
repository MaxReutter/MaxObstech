#!/usr/bin/python
import sys
from datetime import datetime,timedelta
import ephem
from math import pi
import pytz

class ephemeridComputer():

    def __init__(self):
        self.Longitude,self.Latitude= -70.7652399*pi/180., -30.4725365*pi/180.

        self.observer = ephem.Observer()
        self.observer.lon, self.observer.lat = self.Longitude, self.Latitude

    def get_Ephems(self,dateB=None):
        if dateB==None:
            dateA = datetime.utcnow()
            dateB = "%s-%02d-%02d %02d:%02d:%02d" % (dateA.year, dateA.month, dateA.day, \
                               dateA.hour, dateA.minute, dateA.second)
        else:
            local = pytz.timezone ("Chile/Continental")
            naive = datetime.strptime (dateB, "%Y-%m-%d %H:%M:%S")
            local_dt = local.localize(naive, is_dst=None)
            utc_dt = local_dt.astimezone(pytz.utc)
            dateB=utc_dt.strftime ("%Y-%m-%d %H:%M:%S")
        self.observer.date=(dateB)
        moon = ephem.Moon()
        moon.compute(self.observer)
        #nnm = ephem.next_new_moon(self.observer.date)
        #pnm = ephem.previous_new_moon(self.observer.date)
        #moon_phase = (ephem.Date(dateB) - ephem.Date(pnm)) / (ephem.Date(nnm) - ephem.Date(pnm)) # phase percentage
        moon_phase=moon.phase
        moon_elevation=moon.alt
        sun =ephem.Sun()
        sun.compute(self.observer)
        sun_elevation=sun.alt
        sidereal_time=self.observer.sidereal_time()

        return sidereal_time,sun_elevation / ephem.degree,moon_elevation/ ephem.degree,moon_phase,dateB

    def get_daynight(self,dateB=None):
        if dateB == None:
            dateA = datetime.utcnow()
            dateB = "%s-%s-%s" % (dateA.year, dateA.month, dateA.day)
        else:
            local = pytz.timezone ("Chile/Continental")
            try:
                naive = datetime.strptime (dateB, "%Y-%m-%d")
                local_dt = local.localize(naive, is_dst=None)
            except:
                naive = datetime.strptime (dateB, "%Y-%m-%d")+ timedelta(hours=1)
                local_dt = local.localize(naive, is_dst=None)

            utc_dt = local_dt.astimezone(pytz.utc)
            dateB=utc_dt.strftime ("%Y/%m/%d")

        self.observer.date=(dateB)
        nightminutes=0
        for i in range(1440):
            self.observer.date+=ephem.minute

            sun =ephem.Sun()
            sun.compute(self.observer)
            sun_elevation=sun.alt
            if sun_elevation/ ephem.degree<=-18.:
                nightminutes+=1
        return nightminutes,1440-nightminutes


if __name__=="__main__":
    computer=ephemeridComputer()
    st,se,me,mp=computer.get_Ephems()
    print "============Ephemerids============"
    print "Date:              ", computer.observer.date
    print "Sidereal Time:     ", st
    print "Sun Elevation:     ", se
    print "Moon Elevation :   ", me
    print "Moom Phase:        ", mp

