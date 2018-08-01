from datetime import datetime
import sys
import WeatherStatistics as WS
import pymysql.cursors
import ephemerids as eph

def Date():
    """Takes the values "year-month-day" and "hour:minute:second" and assigns
    the right format to "dateB", so that
    "observer.date" and "ephem.Date()" can read it."""
    if len(sys.argv) == 3:
        #dateA = sys.argv[1] + " " + sys.argv[2]
        #print "DATEA: ", dateA
        date_array = sys.argv[1].split("-")
        year = date_array[0]
        month = date_array[1]
        day = date_array[2]
        time_array = sys.argv[2].split(":")
        hour = time_array[0]
        minute = time_array[1]
        second = time_array[2]
        dateB = "%s/%s/%s %s:%s:%s" % (year, month, day, hour, minute, second)
    else:
        dateA = datetime.now()
        dateB = "%s/%s/%s %02d:%02d:%02d" % (dateA.year, dateA.month, dateA.day, \
        dateA.hour, dateA.minute, dateA.second)

    return dateB

if __name__=="__main__":
    #print Date()
    #da = datetime.utcnow()
    #print "%s/%s/%s %02d:%02d:%02d" % (da.year, da.month, da.day, da.hour, da.minute, da.second) # da time NIGGA!
    #print WS.db_connect( )
    moments = open('list', 'r').readlines()
    for moment in moments:
        compu =  eph.ephemeridComputer()
        print moment
        print compu.get_Ephems()
