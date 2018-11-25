#!/usr/bin/python
import matplotlib
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

def populatedb():
    measurementsarray=["Weather1Logs-2017-05-26.txt",  "Weather1Logs-2017-06-07.txt",  "Weather1Logs-2017-06-19.txt",  "Weather1Logs-2017-07-02.txt",
           "Weather1Logs-2017-07-15.txt",  "Weather1Logs-2017-07-28.txt",  "Weather1Logs-2017-08-12.txt",
           "Weather1Logs-2017-05-27.txt",  "Weather1Logs-2017-06-08.txt",  "Weather1Logs-2017-06-20.txt",  "Weather1Logs-2017-07-03.txt",
           "Weather1Logs-2017-07-16.txt",  "Weather1Logs-2017-07-29.txt",  "Weather1Logs-2017-08-13.txt" ,
           "Weather1Logs-2017-05-28.txt",  "Weather1Logs-2017-06-09.txt",  "Weather1Logs-2017-06-21.txt",  "Weather1Logs-2017-07-04.txt",
           "Weather1Logs-2017-07-17.txt",  "Weather1Logs-2017-07-30.txt",  "Weather1Logs-2017-08-14.txt",
           "Weather1Logs-2017-05-29.txt",  "Weather1Logs-2017-06-10.txt",  "Weather1Logs-2017-06-22.txt",  "Weather1Logs-2017-07-05.txt",
           "Weather1Logs-2017-07-18.txt",  "Weather1Logs-2017-07-31.txt",  "Weather1Logs-2017-08-15.txt",
           "Weather1Logs-2017-05-30.txt",  "Weather1Logs-2017-06-11.txt",  "Weather1Logs-2017-06-23.txt",  "Weather1Logs-2017-07-07.txt",
           "Weather1Logs-2017-07-19.txt",  "Weather1Logs-2017-08-03.txt",  "Weather1Logs-2017-08-16.txt",
           "Weather1Logs-2017-05-31.txt",  "Weather1Logs-2017-06-12.txt",  "Weather1Logs-2017-06-24.txt",  "Weather1Logs-2017-07-08.txt",
           "Weather1Logs-2017-07-20.txt",  "Weather1Logs-2017-08-04.txt",  "Weather1Logs-2017-08-17.txt",
           "Weather1Logs-2017-06-01.txt",  "Weather1Logs-2017-06-13.txt",  "Weather1Logs-2017-06-25.txt",  "Weather1Logs-2017-07-09.txt",
           "Weather1Logs-2017-07-21.txt",  "Weather1Logs-2017-08-05.txt",  "Weather1Logs-2017-08-18.txt",
           "Weather1Logs-2017-06-02.txt",  "Weather1Logs-2017-06-14.txt",  "Weather1Logs-2017-06-27.txt",
           "Weather1Logs-2017-07-22.txt",  "Weather1Logs-2017-08-06.txt",  "Weather1Logs-2017-08-19.txt",
           "Weather1Logs-2017-06-03.txt",  "Weather1Logs-2017-06-15.txt",  "Weather1Logs-2017-06-28.txt",  "Weather1Logs-2017-07-11.txt",
           "Weather1Logs-2017-07-23.txt",  "Weather1Logs-2017-08-07.txt",  "Weather1Logs-2017-08-20.txt",
           "Weather1Logs-2017-06-04.txt",  "Weather1Logs-2017-06-16.txt",  "Weather1Logs-2017-06-29.txt",  "Weather1Logs-2017-07-12.txt",
           "Weather1Logs-2017-07-24.txt",  "Weather1Logs-2017-08-08.txt",  "Weather1Logs-2017-08-21.txt",
           "Weather1Logs-2017-06-06.txt",  "Weather1Logs-2017-06-18.txt",  "Weather1Logs-2017-07-01.txt",  "Weather1Logs-2017-07-14.txt",
           "Weather1Logs-2017-07-27.txt" , "Weather1Logs-2017-08-11.txt"  ]
    for datestr in measurementsarray:
        analyzedate(datestr)


def analyzedate(datestr):

    with open(datestr, "r+") as outputfile:
        textdata = outputfile.readlines()
        for line in textdata:
            print line
            if len(line)>5:
                AnalyzeWeatherData(line)
                print line
def analyze_night_humidity(date_init,date_end):
    humidity_data='SELECT humidity,id,fecha FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND sqm>17 )' \
             %(date_init,date_end)
    [db_cursor, db] = db_connect()
    db_cursor.execute(humidity_data)
    res=db_cursor.fetchall()
    humidity = array([item[0] for item in res])
    index=array([item[1] for item in res])
    fecha=array([item[2] for item in res])
    mean_humidity= mean(humidity)
    print mean_humidity
    return mean_humidity

def plot_night_humidity(n_days):
    dates=[]
    humidity_data=[]
    for i in range(n_days):
        print i," days ago"
        dateini=(datetime.datetime.today()- datetime.timedelta(i+1)).__str__().split(" ")[0]
        dateend=(datetime.datetime.today()- datetime.timedelta(i)).__str__().split(" ")[0]
        dates.append(dateini)
        humidity_data.append(analyze_night_humidity(dateini,dateend))

    plt.figure()
    plt.title("El Sauce Yearly night humidity statistics Graph")
    plt.ylabel("Night mena humidity ($^\%$)")
    xfmt = mpldates.DateFormatter('%Y-%m-%d')
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=50, fontsize=8)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(xfmt)
    timestamp2 = [dateutil.parser.parse(s) for s in dates]
    plt.plot(timestamp2, array(humidity_data), label="Night mean humidity",color="blue")

    plt.legend(loc=2, prop={'size': 6})
    statsfile = str(datetime.date.today() - datetime.timedelta(1)) + "humiditystats.png"
    plt.savefig(statsfile)
    plt.show()


def analyseskytemp(date_init,date_end):
    tempdata='SELECT temperature_external,temperature_sky,id,fecha FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND temperature_sky - temperature_external <= -22.5- (temperature_external -10.)/3. and sqm>17 )' \
               %(date_init,date_end)
    tempdata2='SELECT temperature_external,temperature_sky,id,fecha FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND temperature_sky - temperature_external > -22.5- (temperature_external -10.)/3. and sqm>17 )' \
             %(date_init,date_end)
    tempdata3='SELECT temperature_external,temperature_sky,id,fecha FROM `weather` WHERE (fecha>"2017-10-17" AND fecha<"2017-10-18" AND temperature_sky - temperature_external <= -22.5- (temperature_external -10.)/3. and sqm>17 )' \

    [db_cursor, db] = db_connect()
    db_cursor.execute(tempdata)
    res=db_cursor.fetchall()
    db_cursor.execute(tempdata2)
    res2=db_cursor.fetchall()

    db_cursor.execute(tempdata3)
    res3=db_cursor.fetchall()
    skytemp = array([item[1] for item in res])
    temp = array([item[0] for item in res])
    index=array([item[2] for item in res])
    fecha=array([item[3] for item in res])

    skytemp2 = array([item[1] for item in res2])
    temp2 = array([item[0] for item in res2])
    index2=array([item[2] for item in res2])
    fecha2=array([item[3] for item in res2])

    skytemp3 = array([item[1] for item in res3])
    temp3= array([item[0] for item in res3])
    index3=array([item[2] for item in res3])
    fecha3=array([item[3] for item in res3])

    #a=polyfit(skytemp,(temp+skytemp)/(skytemp),3)
    #print a
    print fecha[where((temp+skytemp<-25) )]
    #print fecha[]
    colors=index/(max(index)/2./pi)
    plt.figure()
    colors2=index2/(max(index2)/2./pi)
    plt.title("El Sauce temperatures relation")
    colors3=index3/(max(index3)/2./pi)
    plt.ylabel("skyTemp")
    plt.xlabel("Temp")

    plt.subplots_adjust(bottom=0.2)
    ax = plt.gca()
    plt.scatter(temp, (skytemp)-1.*temp,c=colors, cmap=cm.Oranges,label="Bright Time",marker="+")
    plt.scatter(temp2, (skytemp2)-1.*temp2 ,c=colors2, cmap=cm.Blues,label="Bright Time",marker="+")
    plt.scatter(temp3, (skytemp3)-1.*temp3 ,c=colors3, cmap=cm.Greens,label="Bright Time",marker="+")
    plt.plot(temp, 1.*temp -30. -1.*temp  )
#=(temp-28)/0.8
    plt.show()



def AnalyzeWeatherData(weatherline):
    weatherline=weatherline.replace("\t"," ")
    weatherdata = weatherline.split(" ")
    print "Weather Data:"
    print weatherdata
    date=weatherdata[0]+ " " + weatherdata[1]
    weatherdata=weatherdata[2:]
    pressure = float(weatherdata[0])
    ambienttemperature = float(weatherdata[1]) - 8.
    humidity = float(weatherdata[2])
    wind = float(weatherdata[3])
    wind_dir=float(weatherdata[4])
    windspeed_2mn_average=float(weatherdata[5])
    windgust=float(weatherdata[6])
    windgust_dir=float(weatherdata[7])
    dew = float(weatherdata[8])
    rain = float(weatherdata[9])
    dailyrain = float(weatherdata[10])
    temperature = float(weatherdata[11])
    skytemp = float(weatherdata[12])
    if skytemp >= 100.:
        skytemp = -10
    light = float(weatherdata[13])
    condensation = int(weatherdata[14])
    vsm = float(weatherdata[15])
    sqm = float(weatherdata[16])

    if humidity > 90.:
        retstatus_str = "High Humidity"
    elif wind > 15.:
        retstatus_str = "High Wind"
    elif dew > temperature - 1.:
        retstatus_str = "Possible Condensation"
    elif skytemp - temperature > -22.5 - (temperature - 10.) / 3.:
        retstatus_str = "Cloudy"
    elif sqm < 8.0:
        retstatus_str = "High Light"
    # elif condensation !=0:
    #	outputfile.write("Condensation         ")
    #	return False, "Condensation"
    else:
        retstatus_str = "Go Science!"


    insert_line(date, pressure, humidity, ambienttemperature, temperature, skytemp, dew, wind_dir,
                wind, windspeed_2mn_average, windgust, windgust_dir, rain, dailyrain, condensation, sqm, vsm,
                retstatus_str)
def db_connect( ):
    database = pymysql.connect(host='108.167.137.51',
                               user="obstecho_aries",
                               password="obstech4860",
                               db="obstecho_test")
    db_cursor = database.cursor()
    return [db_cursor, database]

def insert_line(date, pressure, humidity, ambienttemperature, temperature, skytemp, dew, wind_dir,
    wind, windspeed_2mn_average, windgust, windgust_dir, rain, dailyrain, condensation, sqm, vsm, retstatus_str):
    [db_cursor, db] = db_connect()
    stmt = "INSERT INTO obstecho_test.weather(fecha, pressure, humidity, temperature_internal, temperature_external, " \
           "temperature_sky, dewpoint, wind_dir, windspeed, windspeed_2mn_average, windgust, windgust_dir, rain, " \
           "dailyrain, condensation,sqm,vsm,weatherstatus) " \
           "VALUES 	('%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%i,%f,%f,'%s')" \
           % (    date, pressure, humidity, ambienttemperature, temperature, skytemp, dew, wind_dir, wind,
                  windspeed_2mn_average, windgust, windgust_dir, rain, dailyrain, condensation, sqm, vsm, retstatus_str)
    print stmt
    db_cursor.execute(stmt)
    db.commit()

def set_ephems(index ,sidereal_time, moonphase, moonelevation,sunelevation,utc ):
    stmt="UPDATE obstecho_test.weather SET SiderealTime='%s', MoonPhase='%f',MoonElevation='%f',SunElevation='%s',UTC='%s' WHERE id='%i';" %(sidereal_time, moonphase,moonelevation,sunelevation,utc,index)
    return stmt

def compute_ephems(limit):
    [db_cursor, db] = db_connect()
    search= 'SELECT id, fecha FROM `weather` WHERE UTC="" ORDER BY id DESC limit %i;' %(limit)
    db_cursor.execute(search)
    res = db_cursor.fetchall()
    computer = ephemerids.ephemeridComputer()
    stmt=""
    for item in res:
        id = int(item[0])
        fecha= str(item[1])
        st,se,me,mp,utc=computer.get_Ephems(fecha)
        stmt+=set_ephems(id,st,mp,me,se,utc)
    print id
    db_cursor.execute(stmt)
    db.commit()
    return len(res)>0

def get_stat_values(date_init,date_end,db_cursor,field):

    mean_field='SELECT AVG(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s")' \
              %(field,date_init,date_end)
    db_cursor.execute(mean_field)
    res_mean_field=db_cursor.fetchall()[0][0]

    min_field='SELECT MIN(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" )' \
              %(field,date_init,date_end)
    db_cursor.execute(min_field)
    res_min_field=db_cursor.fetchall()[0][0]

    max_field='SELECT MAX(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" )' \
             %(field,date_init,date_end)
    db_cursor.execute(max_field)
    res_max_field=db_cursor.fetchall()[0][0]

    mean_field_day='SELECT AVG(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s"AND SunElevation>=0)' \
              %(field,date_init,date_end)
    db_cursor.execute(mean_field_day)
    res_mean_field_day=db_cursor.fetchall()[0][0]

    min_field_day='SELECT MIN(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND SunElevation>=0)' \
             %(field,date_init,date_end)
    db_cursor.execute(min_field_day)
    res_min_field_day=db_cursor.fetchall()[0][0]

    max_field_day='SELECT MAX(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s"  AND SunElevation>=0)' \
             %(field,date_init,date_end)
    db_cursor.execute(max_field_day)
    res_max_field_day=db_cursor.fetchall()[0][0]


    mean_field_night='SELECT AVG(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s"AND SunElevation<0)' \
                  %(field,date_init,date_end)
    db_cursor.execute(mean_field_night)
    res_mean_field_night=db_cursor.fetchall()[0][0]

    min_field_night='SELECT MIN(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND SunElevation<0)' \
                 %(field,date_init,date_end)
    db_cursor.execute(min_field_night)
    res_min_field_night=db_cursor.fetchall()[0][0]

    max_field_night='SELECT MAX(%s) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s"  AND SunElevation<0)' \
                 %(field,date_init,date_end)
    db_cursor.execute(max_field_night)
    res_max_field_night=db_cursor.fetchall()[0][0]



    return res_mean_field,res_mean_field_day,res_mean_field_night,res_min_field,res_min_field_day,res_min_field_night,res_max_field,res_max_field_day,res_max_field_night


def compute_observed_statistics(date_init,date_end):
    computer = ephemerids.ephemeridComputer()
    nightminutes,dayminutes=computer.get_daynight(date_init)
    [db_cursor, db] = db_connect()
    nightclear='SELECT COUNT(*) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND weatherstatus="Go Science!" AND SunElevation<=-18)' \
        %(date_init,date_end)
    db_cursor.execute(nightclear)
    res_nightclear=db_cursor.fetchall()[0][0]



    nightpossibleclouds='SELECT COUNT(*) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND weatherstatus="Go Science!"AND temperature_sky-temperature_external>-15 AND SunElevation<=-18)' \
        %(date_init,date_end)
    db_cursor.execute(nightpossibleclouds)
    res_nighpossibleclouds=db_cursor.fetchall()[0][0]


    nightbad='SELECT COUNT(*) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND weatherstatus!="Go Science!" AND SunElevation<=-18)' \
        %(date_init,date_end)
    db_cursor.execute(nightbad)
    res_nightbad=db_cursor.fetchall()[0][0]

    daybad='SELECT COUNT(*) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s" AND temperature_sky-temperature_external>-15 AND SunElevation>-18)' \
             %(date_init,date_end)
    db_cursor.execute(daybad)
    res_daybad=db_cursor.fetchall()[0][0]

    twilight='SELECT COUNT(*) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s"  AND SunElevation>-18 AND  SunElevation<=0)' \
           %(date_init,date_end)
    db_cursor.execute(twilight)
    res_twilight=db_cursor.fetchall()[0][0]


    bright='SELECT COUNT(*) FROM `weather` WHERE (fecha>"%s" AND fecha<"%s"  AND SunElevation>-18)'\
        %(date_init,date_end)
    db_cursor.execute(bright)
    res_bright=db_cursor.fetchall()[0][0]


    res_downtime= max(0,1440-(res_nightbad+res_nightclear+res_bright))
    res_downtime_day=max(0,dayminutes-(res_bright))
    res_downtime_night=max(0,nightminutes-(res_nightbad+res_nightclear))

    me_tem,me_temd,me_temn,mi_tem,mi_temd,mi_temn,ma_tem,ma_temd,ma_temn=get_stat_values(date_init,date_end,db_cursor,"temperature_external")
    me_hum, me_humd, me_humn, mi_hum, mi_humd, mi_humn, ma_hum, ma_humd, ma_humn=get_stat_values(date_init,date_end,db_cursor,"humidity")
    res_measured=res_nightbad+res_nightclear+res_bright
    datecount='SELECT COUNT(*) FROM `WeatherDailyStats` WHERE (Date="%s" )' \
           %(date_init)
    db_cursor.execute(datecount)
    res_datecount=db_cursor.fetchall()[0][0]
    if res_datecount==0 and res_measured>0:
        try:
            stmt = "INSERT INTO obstecho_test.WeatherDailyStats(Date, DayMinutes, NightMinutes, DayMeasured, NightMeasured, TotalMeasured," \
           "TwilightMinutes,DayDownTime, NightDownTime, TotalDownTime, DayBadWeather, NightBadWeather, TotalBadWeather,mean_temperature,min_temperature,max_temperature,mean_temperature_day,min_temperature_day,max_temperature_day,mean_temperature_night,min_temperature_night,max_temperature_night,mean_humidity,min_humidity,max_humidity,mean_humidity_day,min_humidity_day,max_humidity_day,mean_humidity_night,min_humidity_night,max_humidity_night) " \
           "VALUES 	('%s',%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)" \
           % (    date_init,dayminutes,nightminutes, res_bright, res_nightbad+res_nightclear, res_nightbad+res_nightclear+res_bright, res_twilight, res_downtime_day, res_downtime_night,
                  res_downtime, res_daybad, res_nightbad+res_nighpossibleclouds, res_daybad+ res_nightbad+res_nighpossibleclouds,me_tem,mi_tem,ma_tem,me_temd,mi_temd,ma_temd,me_temn,mi_temn,ma_temn,me_hum, mi_hum, ma_hum, me_humd, mi_humd, ma_humd, me_humn, mi_humn, ma_humn)
            print stmt

            db_cursor.execute(stmt)
            db.commit()
        except:
            print  "failed!"


    return res_nightclear-res_nighpossibleclouds,res_nightbad+res_nighpossibleclouds,res_bright,res_nighpossibleclouds,res_downtime, dayminutes,nightminutes, res_daybad,res_twilight,res_downtime_day,res_downtime_night

def compute_yearlystats(ndays,plotdata=True):
    dates=[]
    cleardata=[]
    badweatherdata=[]
    brightdata=[]
    downdata=[]
    daybad_data=[]
    twilight_data=[]
    night_data=[]
    downday_data=[]
    downnight_data=[]
    for i in reversed(range(ndays)):
        print i," days ago"
        dateini=(datetime.datetime.today()- datetime.timedelta(i+1)).__str__().split(" ")[0]
        dateend=(datetime.datetime.today()- datetime.timedelta(i)).__str__().split(" ")[0]
        [clear,bad,bright,possibleclouds,down,day,night, daybad,twilight,downday,downnight]=compute_observed_statistics(dateini,dateend)
        print dateini, possibleclouds
        if (clear+bad)>0:
            dates.append(dateini)
            cleardata.append(float(clear)/(clear+bad))
            badweatherdata.append(float(bad)/float(day+night))
            brightdata.append(float(day)/float(day+night))
            night_data.append(float(night)/float(day+night))
            downdata.append(float(down)/float(day+night))
            daybad_data.append(float(daybad)/float(day+night))
            twilight_data.append(float(twilight)/float(day+night))
            downday_data.append(float(downday)/float(day+night))
            downnight_data.append(float(downnight)/float(day+night))

    print len(cleardata),min(cleardata),max(cleardata)
    if plotdata:
        plt.figure(figsize=(10,6))
        plt.title("El Sauce Yearly statistics Graph\n Clear Time= %4.1f%s (%i nights/year) " %(np.mean(cleardata)*100.,"%",np.mean(cleardata)*365))
        plt.ylabel("Time ($^\%$)")
        xfmt = mpldates.DateFormatter('%Y-%m-%d')
        plt.subplots_adjust(bottom=0.2)
        plt.xticks(rotation=50, fontsize=8)
        ax = plt.gca()
        ax.xaxis.set_major_formatter(xfmt)
        timestamp2 = [dateutil.parser.parse(s) for s in dates]
        plt.bar(timestamp2, array(badweatherdata)*0.+1., label="Bad Weather",color="lightgrey")
        plt.bar(timestamp2, 1-array(daybad_data), label="Day Donwtime",color="red")
        plt.bar(timestamp2, 1-array(daybad_data)-array(downday_data), label="Day time",color="white")
        plt.bar(timestamp2, 1-array(brightdata)+array(twilight_data), label="Twilight",color="blue")
        plt.bar(timestamp2, array(night_data), label="Clear Time",color="black")

    #    plt.plot(timestamp2, 1-array(brightdata), label="Bright Time",color="white")
        plt.plot(timestamp2, 1-array(brightdata), label="Clear Time",color="black")
        d = np.zeros(len(brightdata))
        d2 = np.ones(len(brightdata))
        ax.fill_between(timestamp2, d2, where=d2 >= 1-array(brightdata), color='white')
        ax.fill_between(timestamp2, 1-array(brightdata), where=1-array(brightdata) >= 0, color='black')
        plt.bar(timestamp2, array(downnight_data)+array(badweatherdata), label="Night DownTime",color="red")
        plt.bar(timestamp2, array(badweatherdata), label="Bad Weather",color="lightgrey")

        #ax.fill_between(timestamp2, array(badweatherdata), where=array(badweatherdata) >= d, color='lightgrey')
        #ax.fill_between(timestamp2, array(downdata), where=array(downdata) >= d, color='red')

        plt.legend(loc=2, prop={'size': 6})
        statsfile = str(datetime.date.today() - datetime.timedelta(1)) + "yearlystats.png"
        plt.savefig(statsfile)
        plt.show()

if __name__=="__main__":
    compute_yearlystats(2,False)

