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
search = "SELECT `UTC`, `sqm` FROM `weather_OVERHAUL` WHERE \
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
y = []
x = []

counter = 0
for e in res:
    #print e
    x.append(counter)
    sqm = e[1]
    y.append(sqm)
    counter += 1

print "There are " + str(counter) + " data points."
plt.scatter(x, y, 0.1, c='black', alpha=0.1, label='data point')
plt.legend()
plt.title('UTC sun:-15 moon:-5 // data points in cronological order')
plt.ylabel('Sky Quality Meter')
ticks = [0, counter-1]
ticks_labels = ['%s' % (res[0][0]), '%s' % (res[-1][0])]
plt.xticks(ticks, ticks_labels)
plt.savefig("alldatapoints_OVERHAUL.png")
plt.show()
