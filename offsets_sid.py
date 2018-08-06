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

#colors = ['r', 'y', 'b', 'greenyellow', 'c', 'g', 'black']

#binSize = 10080 # data points, one per minute, 10.080 a week
[db_cursor, database] = WS.db_connect()
search = "SELECT `UTC`, `sqm`, `SiderealTime` FROM `weather` WHERE \
`UTC` > '2017-08-05 10:17:15' AND `UTC` <= '2018-12-01 01:08:24' AND \
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC LIMIT 1000000"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
# y = []
# x = []
# offset = 0.7-3.2+2.09+0.32-0.28-0.11-0.19-0.29+0.28+0.34
# y2 = []
# x2 = []
# offset2 = 0.7+2.09+0.32-0.28-0.11-0.19-0.29+0.28+0.34
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
counter = 0
for e in res:
    #print e[2][0:5]
    # if e[0] <= '2017-07-04 10:29:14':
    # 	x.append(e[2][0:5])
    # 	y.append(e[1] + offset)
    # elif e[0] <= '2017-08-05 10:17:15':
    #     x2.append(e[2][0:5])
    # 	y2.append(e[1] + offset2)
    if e[0] <= '2017-11-30 08:15:29':
        x3.append(e[2][0:5])
    	y3.append(e[1] + offset3)
    elif e[0] <= '2018-01-29 08:54:35':
        x4.append(e[2][0:5])
    	y4.append(e[1] + offset4)
    elif e[0] <= '2018-02-04 01:46:23':
        x5.append(e[2][0:5])
    	y5.append(e[1] + offset5)
    elif e[0] <= '2018-02-07 03:34:24':
        x6.append(e[2][0:5])
    	y6.append(e[1] + offset6)
    elif e[0] <= '2018-02-08 04:10:21':
        x7.append(e[2][0:5])
    	y7.append(e[1] + offset7)
    elif e[0] <= '2018-02-09 03:19:30':
        x8.append(e[2][0:5])
    	y8.append(e[1] + offset8)
    elif e[0] <= '2018-02-22 09:19:23':
        x9.append(e[2][0:5])
    	y9.append(e[1] + offset9)
    counter += 1

print "There are " + str(counter) + " data points."
# plt.scatter(x, y, 1, c='black', alpha=0.05, label='data point')
# plt.scatter(x2, y2, 1, c='r', alpha=0.05, label='data point')
plt.scatter(x3, y3, 1, c='black', alpha=0.05, label='data point')
plt.scatter(x4, y4, 1, c='black', alpha=0.05, label='data point')
plt.scatter(x5, y5, 1, c='black', alpha=0.05, label='data point')
plt.scatter(x6, y6, 1, c='black', alpha=0.05, label='data point')
plt.scatter(x7, y7, 1, c='black', alpha=0.05, label='data point')
plt.scatter(x8, y8, 1, c='black', alpha=0.05, label='data point')
plt.scatter(x9, y9, 1, c='black', alpha=0.05, label='data point')
plt.legend()
plt.title('Sidereal time // sun:-15 moon:-5 // offsets applied')
plt.ylabel('Sky Quality Meter')
ticks = ['00:00', '24:00']
ticks_labels = ['0hrs', '24hrs']
time_start = time(0,0,0)
time_end = time(24,0,0)
ticks = [time_start, time_end]
ticks_labels = [time_start, time_end]
plt.xticks(ticks, ticks_labels)
plt.savefig("offsets_sid.png")
plt.show()
