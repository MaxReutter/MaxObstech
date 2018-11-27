######### DESCRIPCION ########################################
# modQM.py
# este programa corrige el SQM de cada dato de 
# weather_calib segun los offsets encontrados
##############################################################

#!/usr/bin/python
import WeatherStatistics as WS
import numpy as np
#matplotlib.use("Agg")
from matplotlib import pyplot as plt
import matplotlib.dates as mpldates
import dateutil
from numpy import append,array,where,pi,polyfit,where,mean
from pylab import cm
import datetime
import pymysql.cursors
import ephemerids

[db_cursor, database] = WS.db_connect()
search = "SELECT `UTC`, `sqm`, `id` \
FROM `weather_calib` \
WHERE `UTC` >= '2017-08-28 15:03:29' \
ORDER BY `UTC` ASC"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0][0], " to ", res[-1][0]
 
offset3 = 0.35+0.32-0.28-0.11-0.19-0.29+0.28+0.34
offset4 = 0.35-0.28-0.11-0.19-0.29+0.28+0.34
offset5 = -0.11-0.19-0.29+0.28+0.34
offset6 = -0.19-0.29+0.28+0.34
offset7 = -0.29+0.28+0.34
offset8 = 0.28+0.34
offset9 = 0.34

for e in res:
    UTC = e[0]
    print UTC
    sqm = e[1]
    ID = e[2]

    if UTC <= '2017-11-30 08:15:29':
        sqm += offset3
    elif UTC <= '2018-01-29 08:54:35':
        sqm += offset4
    elif UTC <= '2018-02-04 01:46:23':
        sqm += offset5
    elif UTC <= '2018-02-07 03:34:24':
        sqm += offset6
    elif UTC <= '2018-02-08 04:10:21':
        sqm += offset7
    elif UTC <= '2018-02-09 03:19:30':
        sqm += offset8
    elif UTC <= '2018-02-22 09:19:23':
        sqm += offset9

    modify = "UPDATE `weather_OVERHAUL` \
    SET `sqm` = '%s' \
    WHERE `id` = '%s'" % (sqm, ID)

    db_cursor.execute(modify)