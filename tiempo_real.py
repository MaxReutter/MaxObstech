#!/usr/bin/python
import sys
from datetime import datetime
import ephem
from Date import Date
from time import sleep

# DATA OBSTECH REVISAR!
longitude, latitude = '-70:45:47', '-30:28:21'

while True:
    # DATA
    dateB = Date()
    observer = ephem.Observer()
    observer.lon, observer.lat = longitude, latitude
    observer.date = (dateB)
    moon = ephem.Moon()
    moon.compute(observer)
    nnm = ephem.next_new_moon(observer.date)
    pnm = ephem.previous_new_moon(observer.date)
    mphase = (ephem.Date(dateB) - ephem.Date(pnm)) / (ephem.Date(nnm) - ephem.Date(pnm)) # phase percentage
    # print "MPHASE: ", mphase
    o_phase = "" # phase output

    # MOON PHASE
    if mphase >= 0 and mphase < 0.125:
        o_phase = "New"
    elif mphase >= 0.125 and mphase < 0.375:
        o_phase = "Cuarter"
    elif mphase >= 0.375 and mphase < 0.625:
        o_phase = "Half"
    elif mphase >= 0.625 and mphase < 0.875:
        o_phase = "Three Cuarters"
    elif mphase >= 0.875 and mphase <= 1:
        o_phase = "Full"
    else:
        print "ERROR, not a valid mphase."
        o_phase = "ERROR"
        break

    # OUTPUT
    print "--------------Moon-------------------"
    print "Date:              ", dateB
    print "Sidereal Time:     ", observer.sidereal_time()
    print "Moon Phase:        ", o_phase
    print "Altitude:          ", moon.alt
    print "Next New Moon:     ", nnm
    print "Previous New Moon: ", pnm

    sleep(1)
