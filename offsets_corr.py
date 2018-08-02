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
search = "SELECT `UTC`, `sqm` FROM `weather` WHERE \
`UTC` >= '2017-01-01 03:29:25' AND `UTC` <= '2018-12-01 01:08:24' AND \
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC LIMIT 1000000"

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
counter = 0
for e in res:
    #print e[0]
    if e[0] <= '2017-07-04 10:29:14':
    	x.append(counter)
    	y.append(e[1] + offset)
    elif e[0] <= '2017-08-05 10:17:15':
        x2.append(counter)
    	y2.append(e[1] + offset2)
    elif e[0] <= '2017-11-30 08:15:29':
        x3.append(counter)
    	y3.append(e[1] + offset3)
    elif e[0] <= '2018-01-29 08:54:35':
        x4.append(counter)
    	y4.append(e[1] + offset4)
    elif e[0] <= '2018-02-04 01:46:23':
        x5.append(counter)
    	y5.append(e[1] + offset5)
    elif e[0] <= '2018-02-07 03:34:24':
        x6.append(counter)
    	y6.append(e[1] + offset6)
    elif e[0] <= '2018-02-08 04:10:21':
        x7.append(counter)
    	y7.append(e[1] + offset7)
    elif e[0] <= '2018-02-09 03:19:30':
        x8.append(counter)
    	y8.append(e[1] + offset8)
    elif e[0] <= '2018-02-22 09:19:23':
        x9.append(counter)
    	y9.append(e[1] + offset9)
    counter += 1

print "There are " + str(counter) + " data points."
plt.scatter(x, y, 0.2, c='black', alpha=1, label='data point')
plt.scatter(x2, y2, 0.2, c='r', alpha=1, label='data point')
plt.scatter(x3, y3, 0.2, c='g', alpha=1, label='data point')
plt.scatter(x4, y4, 0.2, c='b', alpha=1, label='data point')
plt.scatter(x5, y5, 0.2, c='y', alpha=1, label='data point')
plt.scatter(x6, y6, 0.2, c='c', alpha=1, label='data point')
plt.scatter(x7, y7, 0.2, c='black', alpha=1, label='data point')
plt.scatter(x8, y8, 0.2, c='r', alpha=1, label='data point')
plt.scatter(x9, y9, 0.2, c='g', alpha=1, label='data point')
plt.legend()
plt.title('UTC-4 sun:-15 moon:-5 // data points in cronological order // offsets applied')
plt.ylabel('Sky Quality Meter')
ticks = [0, counter-1]
ticks_labels = ['%s' % (res[0][0]), '%s' % (res[-1][0])]
plt.xticks(ticks, ticks_labels)
plt.savefig("offsets_corr.png")
plt.show()
