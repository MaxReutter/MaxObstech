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

colors = ['r', 'y', 'b', 'greenyellow', 'c', 'g', 'black']

[db_cursor, database] = WS.db_connect()
search = "SELECT `UTC`, `sqm` FROM `weather` WHERE \
`UTC` >= '2017-01-01 03:29:25' AND `UTC` <= '2018-12-25 01:08:24' AND \
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC LIMIT 1000000"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
y = []
x = []
counter = 0
for e in res:
    #print e
    x.append(counter)
    y.append(e[1])
    counter += 1

print "There are " + str(counter) + " data points."
plt.scatter(x, y, 0.2, c='black', alpha=1, label='data point')
plt.legend()
plt.title('UTC-4 sun:-15 moon:-5 // data points in cronological order')
plt.ylabel('Sky Quality Meter')
ticks = [0, counter-1]
ticks_labels = ['%s' % (res[0][0]), '%s' % (res[-1][0])]
plt.xticks(ticks, ticks_labels)
plt.savefig("1_alldatapoints.png")
plt.show()
