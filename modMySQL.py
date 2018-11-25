######### DESCRIPCION ########################################
# modMySQL.py
# UTC calculado para datos entre '2018-04-29 14:44:32' y 
# '2018-05-12 22:59:38' (suponiendo que fecha esta en formato 
# UTC-4 durante horario de invierno.
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
WHERE `id` > '450918' \
AND `id` < '469891'"

db_cursor.execute(search)
res = db_cursor.fetchall()
print "From ", res[0], " to ", res[-1]

for e in res:
    fecha = e[0]
    delta = datetime.timedelta(hours=3)
    UTC = fecha + delta
    id = e[1]
    print id

    modify = "UPDATE `weather_calib` \
    SET `UTC` = '%s' \
    WHERE `id` = '%s'" % (UTC, id)

    db_cursor.execute(modify)