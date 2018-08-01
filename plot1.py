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

colors = [
'r', 'y', 'b', 'greenyellow', 'c', 'g', 'black', \
'r', 'y', 'b', 'greenyellow', 'c', 'g', 'black', \
'r', 'y', 'b', 'greenyellow', 'c', 'g', 'black', \
'r', 'y', 'b', 'greenyellow', 'c', 'g', 'black', \
'gray', 'gray', 'gray'] # 31 days

[db_cursor, database] = WS.db_connect()
search = "SELECT `UTC`, `sqm` FROM `weather` WHERE \
 `UTC` >= '2017-06-01 23:00:00' AND `UTC` <= '2017-07-01 11:00:00' AND\
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC LIMIT 1000000"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
y = []
x = []
#prevDay = int(res[0][0][8:10])
counter = 0
for e in res:
    counter += 1
    UTCObstech = -4
    day = int(e[0][8:10])
    hour = UTCObstech + int(e[0][11:13]) + 24 # para siempre trabajar solo con positivos incluso sumando UTC-23
    minute = int(e[0][14:16])
    second = int(e[0][17:19])
    t = hour*60*60 + minute*60 + second # seconds from 19*60*60 (7pm) to (24 + 7)*60*60 (7am)
    if hour >= 19 + 24:
        x.append(t)
        y.append(e[1])
    elif hour <= 7 + 24:
        x.append(t + 24*60*60)
        y.append(e[1])

plt.scatter(x, y, 0.3, c='b', alpha=0.2)

[db_cursor, database] = WS.db_connect()
search = "SELECT `UTC`, `sqm` FROM `weather` WHERE \
`UTC` >= '2017-07-01 23:00:00' AND `UTC` <= '2017-08-01 11:00:00' AND\
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC LIMIT 1000000"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
x2 = []
y2 = []
#prevDay = int(res[0][0][8:10])
counter = 0
for e in res:
    counter += 1
    UTCObstech = -4
    day = int(e[0][8:10])
    hour = UTCObstech + int(e[0][11:13]) + 24 # para siempre trabajar solo con positivos incluso sumando UTC-23
    minute = int(e[0][14:16])
    second = int(e[0][17:19])
    t = hour*60*60 + minute*60 + second # seconds from 19*60*60 (7pm) to (24 + 7)*60*60 (7am)
    if hour >= 19 + 24:
        # print e[1]
        # print hour
        # print minute
        # print second
        # print t
        x2.append(t)
        y2.append(e[1])
    elif hour <= 7 + 24:
        x2.append(t + 24*60*60)
        y2.append(e[1])

plt.scatter(x2, y2, 0.3, c='r', alpha=0.2)

[db_cursor, database] = WS.db_connect()
search = "SELECT `UTC`, `sqm` FROM `weather` WHERE \
`UTC` >= '2017-08-01 23:00:00' AND `UTC` <= '2017-09-01 11:00:00' AND\
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC LIMIT 1000000"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
x3 = []
y3 = []
#prevDay = int(res[0][0][8:10])
counter = 0
for e in res:
    counter += 1
    UTCObstech = -4
    day = int(e[0][8:10])
    hour = UTCObstech + int(e[0][11:13]) + 24 # para siempre trabajar solo con positivos incluso sumando UTC-23
    minute = int(e[0][14:16])
    second = int(e[0][17:19])
    t = hour*60*60 + minute*60 + second # seconds from 19*60*60 (7pm) to (24 + 7)*60*60 (7am)
    if hour >= 19 + 24:
        # print e[1]
        # print hour
        # print minute
        # print second
        # print t
        x3.append(t)
        y3.append(e[1])
    elif hour <= 7 + 24:
        x3.append(t + 24*60*60)
        y3.append(e[1])

plt.scatter(x3, y3, 0.3, c='g', alpha=0.2)

    # day = int(e[0][8:10])
    # if day > prevDay:
    #     prevDay = day
    #     color = colors[day - 1]
    #     plt.scatter(x, y, 0.3, c=color, alpha=1)
    #     x = []
    #     y = []

print "There are " + str(counter) + " data points."

plt.title('UTC-4 sun:-15 moon:-5')
plt.ylabel('Sky Quality Meter')
# ticks = ['19:00:00','20:00:00','21:00:00','22:00:00','23:00:00','24:00:00', \
# '25:00:00','26:00:00','27:00:00','28:00:00','29:00:00','30:00:00','31:00:00']
ticks = [(24+19)*60*60, (24+20)*60*60, (24+21)*60*60, (24+22)*60*60, (24+23)*60*60, (24+24)*60*60, (24+25)*60*60, \
(24+26)*60*60, (24+27)*60*60, (24+28)*60*60, (24+29)*60*60, (24+30)*60*60, (24+31)*60*60]
ticks_labels = ['7pm', '8pm', '9pm', '10pm', '11pm', '12pm', '1am', '2am', \
'3am', '4am', '5am', '6am', '7am']
plt.xticks(ticks, ticks_labels)
plt.savefig("1_1.png")
plt.show()
