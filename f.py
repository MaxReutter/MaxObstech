from datetime import datetime
import ephem

# data google
degrees ,latitude = '-70.763043', '-30.472549'
elevation = 1500

def degrees_to_full(degrees):
    # adaptation of position format
    deg_front = degrees.split('.')[0]
    deg_back = float(degrees.split('.')[1])
    deg_back = str(deg_back)
    deg_back = deg_back[:2] + '.' + deg_back[2:]
    print 'deg_back: ', deg_back
    degrees_degrees = deg_front
    print degrees_degrees
    minutes = str(float(deg_back) / 100.0 * 60)
    minutes_front = minutes.split('.')[0]
    degrees_minutes = minutes_front
    min_back = deg_back.split('.')[1]
    min_back = min_back[:2] + '.' + min_back[2:]
    seconds = str(float(min_back / 100.0 * 60))
    degrees_seconds = seconds.split('.')[0]
    seconds_leftover = seconds.split('.')[1]

    return degrees_degrees, degrees_minutes, degrees_seconds

time = datetime.now()
print(time)
#observer.date = time
#siderealtime = observer.sidereal_time()

observer = ephem.Observer()
observer.lon, observer.lat = degrees, latitude
observer.elevation = elevation
observer.date = '%s/%s/%s %s:%s' % (time.year, time.day, time.month, \
time.hour, time.minute) # input format: 'year/day/month hour:minute'
print(observer.sidereal_time())
