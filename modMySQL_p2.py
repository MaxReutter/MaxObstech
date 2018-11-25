######### DESCRIPCION ###########################################
# modMySQL_p2.py
# Primer set de datos (id 469891 a 469950) de la hora del cambio 
# de hora, estos aun son fecha en UTC-3. Despues segundo set de 
# datos (id 469951 a 470010), estos ya son fecha en UTC-4.
# O almenos parto desde esa idea.
#################################################################

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
WHERE `id` > '469890' \
AND `id` < '469951'"

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