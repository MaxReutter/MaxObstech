# s = '9:'
# n = int(s[0:4])
# print n

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
search = "SELECT `UTC`,`SiderealTime`,`sqm` FROM `weather` WHERE \
`UTC` <= '2018-04-28 07:00:00' AND `UTC` >= '2017-04-28 19:00:00' AND\
`SunElevation` < -15 AND `MoonElevation` < -5 AND \
`weatherstatus`= 'Go Science!' ORDER BY `UTC` ASC LIMIT 150000"
db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]
y = []
x = []
for e in res:
    # print e[1]
    # print len(e[1])
    if len(e[1]) == 10:
        hour = int(e[1][0])
        minute = int(e[1][2:4])
        second = int(e[1][5:7])
    else: # len = 11
        hour = int(e[1][0:2])
        minute = int(e[1][3:5])
        second = int(e[1][6:8])
    t = hour*60*60 + minute*60 + second # seconds from 19*60*60 (7pm) to (24 + 7)*60*60 (7am)
    if (hour >= 19) or (hour <= 7):
        # print e[1]
        # print hour
        # print minute
        # print second
        # print t
        if hour <= 7:
            x.append(t + 24*60*60)
            y.append(e[2])
        else:
            x.append(t)
            y.append(e[2])
    #else:
        #print e[1], " is not in range 7pm to 7am"
        # print

# y_temp = []
# x_temp = []
# counter = 0
# chunksize = 1 # OJO! LIMIT debe ser divisible entero por chunksize
# for e in res:
#     #print e[2]
#     y_temp.append(e[2])
#     counter += 1
#     #print counter
#     if counter == chunksize:
#         counter = 0
#         sum = 0
#         for i in y_temp:
#             #print i
#             sum += float(i)
#             #print sum
#         average = float(sum) / chunksize
#         for i in range(chunksize):
#             y.append(average)
#             x.append(i)
#
#         y_temp = []
#         #print y
#         #print x
#
plt.scatter(x, y, 0.1, alpha=1)
plt.ylabel('Sky Quality Meter')
# ticks = ['19:00:00','20:00:00','21:00:00','22:00:00','23:00:00','24:00:00', \
# '25:00:00','26:00:00','27:00:00','28:00:00','29:00:00','30:00:00','31:00:00']
ticks = [19*60*60, 20*60*60, 21*60*60, 22*60*60, 23*60*60, 24*60*60, 25*60*60, \
26*60*60, 27*60*60, 28*60*60, 29*60*60, 30*60*60, 31*60*60]
ticks_labels = ['7pm', '8pm', '9pm', '10pm', '11pm', '12pm', '1am', '2am', \
'3am', '4am', '5am', '6am', '7am']
plt.xticks(ticks, ticks_labels)
plt.savefig("2_1.png")
plt.show()
