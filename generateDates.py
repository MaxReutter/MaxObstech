from datetime import datetime

def generateDates():
    today = datetime.now
    today = strip(today(" ", "-", ":"))
    list = open("list", "w")
    for day in range(30):
        for hour in range(24):
            list.writeln("%s-%s-%s %02d:%02d:%02d" % (today[0]-30+day,today[1], today[2],today[3]-24+hour, today[4], today[5])
