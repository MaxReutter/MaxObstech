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
from datetime import datetime
import matplotlib.dates as mdates

[db_cursor, database] = WS.db_connect()
search = "SELECT `fecha`, `sqm` FROM `weather` WHERE \
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `fecha` ASC"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
y = []
x = []
offset = 0.7-3.2+2.09+0.32-0.28-0.11-0.19-0.29+0.28+0.34
y2 = []
x2 = []
offset2 = 0.7+2.09+0.32-0.28-0.11-0.19-0.29+0.28+0.34
y3 = []
x3 = []
offset3 = 0.35+0.32-0.28-0.11-0.19-0.29+0.28+0.34
y4 = []
x4 = []
offset4 = 0.35-0.28-0.11-0.19-0.29+0.28+0.34
y5 = []
x5 = []
offset5 = -0.11-0.19-0.29+0.28+0.34
y6 = []
x6 = []
offset6 = -0.19-0.29+0.28+0.34
y7 = []
x7 = []
offset7 = -0.29+0.28+0.34
y8 = []
x8 = []
offset8 = 0.28+0.34
y9 = []
x9 = []
offset9 = 0.34
x10 = []
y10 = []
counter = 0
for e in res:
    #print e[0]
    date = datetime.strptime(e[0], '%Y-%m-%d %H:%M:%S')
    time = date
    # if (date.hour-4)  >= 0 and (date.hour-4) < 12:
    #     time = datetime(1900,1,2,(date.hour-4),date.minute,date.second,0)
    # elif (date.hour-4) < 0:
    #     time = datetime(1900,1,1,24+(date.hour-4),date.minute,date.second,0)
    # else:
    #     time = datetime(1900,1,1,(date.hour-4),date.minute,date.second,0)
    if e[0] <= '2017-07-04 10:29:14':
    	x.append(time)
    	y.append(e[1] + offset)
    elif e[0] <= '2017-08-05 10:17:15':
        x2.append(time)
    	y2.append(e[1] + offset2)
    elif e[0] <= '2017-11-30 08:15:29':
        x3.append(time)
    	y3.append(e[1] + offset3)
    elif e[0] <= '2018-01-29 08:54:35':
        x4.append(time)
    	y4.append(e[1] + offset4)
    elif e[0] <= '2018-02-04 01:46:23':
        x5.append(time)
    	y5.append(e[1] + offset5)
    elif e[0] <= '2018-02-07 03:34:24':
        x6.append(time)
    	y6.append(e[1] + offset6)
    elif e[0] <= '2018-02-08 04:10:21':
        x7.append(time)
    	y7.append(e[1] + offset7)
    elif e[0] <= '2018-02-09 03:19:30':
        x8.append(time)
    	y8.append(e[1] + offset8)
    elif e[0] <= '2018-02-22 09:19:23':
        x9.append(time)
    	y9.append(e[1] + offset9)
    else:
        x10.append(time)
        y10.append(e[1])
    counter += 1

print "There are " + str(counter) + " data points."
plt.scatter(x, y, 0.2, c='black', alpha=1)
plt.scatter(x2, y2, 0.2, c='r', alpha=1)
plt.scatter(x3, y3, 0.05, c='black', alpha=0.05)
plt.scatter(x4, y4, 0.05, c='black', alpha=0.05)
plt.scatter(x5, y5, 0.05, c='black', alpha=0.05)
plt.scatter(x6, y6, 0.05, c='black', alpha=0.05)
plt.scatter(x7, y7, 0.05, c='black', alpha=0.05)
plt.scatter(x8, y8, 0.05, c='black', alpha=0.05)
plt.scatter(x9, y9, 0.05, c='black', alpha=0.05)
plt.scatter(x10, y10, 0.05, c='black', alpha=0.05)
#plt.legend()
plt.title('UTC // sun:-15 moon:-5 // first months filtered // offsets applied')
plt.ylabel('Sky Quality Meter')
# time_start = datetime(1900,1,1,19,0,0,0)
# time_end = datetime(1900,1,2,6,59,59,999999)
#'2017-08-05 10:17:15'
#'2018-08-11 00:44:30'
time_start = datetime(2017,8,5,10,17,15,0)
time_end = datetime(2018,8,11,0,44,30,0)
plt.xlim(time_start, time_end)
plt.grid(True)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.savefig("offsets_corr5.png")
plt.show()
