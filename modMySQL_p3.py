############### DESCRIPCION ##################################
# modMySQL_p3.py
# Los datos despues de p2 (id 470011 a 576186), es decir desde 
# 13 Mayo hasta el 2018-07-27 14:42:44. Son horario invierno, 
# es decir UTC-4. 
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
search = "SELECT `fecha`, `id` FROM `weather_calib` \
WHERE `id` >= '470011' \
AND `id` <= '576186'"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]

for e in res:
    fecha = e[0]
    delta = datetime.timedelta(hours=4)
    UTC = fecha + delta
    id = e[1]
    print id

    modify = "UPDATE `weather_calib` \
    SET `UTC` = '%s' \
    WHERE `id` = '%s'" % (UTC, id)

    db_cursor.execute(modify)