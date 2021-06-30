def add_time(start, duration, day = ''):
    if 'AM' in start:
        stripstart = start.strip('AM')
    else:
        stripstart = start.strip('PM')

    #daylist where Monday = 0
    daylist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    hoursfromstart = int(stripstart.split(':')[0])
    minutesfromstart = int(stripstart.split(':')[1])
    hoursfromduration = int(duration.split(':')[0])
    minutesfromduration = int(duration.split(':')[1])
    timeperiods = ''

    if 'PM' in start:
        hoursfromstart += 12
    
    addedhours = hoursfromstart + hoursfromduration 
    addedminutes = minutesfromstart + minutesfromduration
    tohour = addedminutes // 60 
    newminutes = addedminutes % 60
    newhours = (addedhours + tohour) % 24
    days = (addedhours + tohour) // 24
    adjminutes = ''
    adjhours = ''

    if newhours <= 11:
        timeperiods = ' AM'
    else:
        timeperiods = ' PM'

    if newhours > 12:
        newhours -= 12
        adjhours = str(newhours)
    elif newhours == 0:
            newhours = 12
            adjhours = str(newhours)
    else:
        adjhours = str(newhours)

    
    if len(str(newminutes)) < 2:
        adjminutes = str(newminutes).zfill(2)
    else:
        adjminutes = str(newminutes)

    
    if not day:
        if days == 0:
            return adjhours + ':' + adjminutes + timeperiods
        if days == 1:
            return adjhours + ':' + adjminutes + timeperiods + ' (next day)'
        else:
            return adjhours + ':' + adjminutes + timeperiods + ' (' + str(days) + ' days later)'
    else:
        mday = day.title()
        if mday in daylist:
            newday = (daylist.index(mday) + days) % 7
            if newday == daylist.index(mday):
                resultday = daylist[newday]
        resultday = daylist[newday]
        if days == 0:
            return adjhours + ':' + adjminutes + timeperiods + ', ' + resultday
        if days == 1:
            return adjhours + ':' + adjminutes + timeperiods + ', ' + resultday + ' (next day)'
        else:
            return adjhours + ':' + adjminutes + timeperiods + ', ' + resultday + ' (' + str(days) + ' days later)'

print(add_time("6:30 AM", "205:12")) #should return 7:42 AM
print(add_time("5:59 PM", "0:01")) #should return 12:00 PM
print(add_time("11:30 AM", "2:32", "Monday")) #should return 2:02 PM
print(add_time("11:43 PM", "25:20", "tueSday")) #should return 12:03 AM, Thursday (2 days later)
print(add_time("12:00 PM", "24:00", "tueSday")) #should return 12:00 PM 2 days  
print(add_time("11:30 PM", "2:32"))