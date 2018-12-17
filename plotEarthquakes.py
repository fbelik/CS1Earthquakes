# str,str -> bool
def dateLessThan(date1,date2):
    """Takes in 2 strings which are dates and returns True
    if date1 is less than date2."""
    return ((date1[:4]<date2[:4]) or (date1[:4]==date2[:4] and date1[5:7]<date2[5:7]) or (date1[:4]==date2[:4] and date1[5:7]==date2[5:7] and date1[8:]<date2[8:]))

# str,str,str -> bool
def betweenDates(date1,date2,date3):
    """Takes in 3 strings which are dates and returns True if
    date 1 is after date 2 and before date 3. Otherwise the
    function returns false."""
    return (dateLessThan(date1,date3) and not dateLessThan(date1,date2))

import urllib.request

# str,str -> list of list of str
def parseEarthquakeData(date1,date2):
    """Takes in two dates, the first one after the
    other, and returns a list of lists. The sub lists
    contain latitude, longitude, magnitude, and depth
    of the earthquakes between the dates."""
    a = urllib.request.urlopen('http://www.choongsoo.info/teach/mcs177-sp12/projects/earthquake/earthquakeData-02-23-2012.txt')
    a.readline()
    data = [i.decode('ascii')[22:-1].split(',') for i in a if betweenDates(i.decode('ascii')[:10],date1,date2)]
    return data

def subtract1(date):
    day = int(date[8:])
    month = int(date[5:7])
    year = int(date[0:4])
    t1s = [2,4,6,8,9,11,1]
    t0s = [5,7,10,12]
    if (day>1 and day>10):
        return date[0:8]+str(day-1)
    elif (day>1):
        return date[0:8]+'0'+str(day-1)
    elif (month in t1s[:5]):
        return date[0:5]+'0'+str(month-1)+'/31'
    elif (month == t1s[5]):
        return date[0:5]+str(month-1)+'/31'
    elif (month == t1s[6]):
        return str(year-1)+'/12/31'
    elif (month in t0s[:3]):
        return date[0:5]+'0'+str(month-1)+'/30'
    elif (month == 12):
        return date[0:5]+str(month-1)+'/30'
    elif (month == 3 and (year%4)!=0):
        return date[0:5]+str(month-1)+'/29'
    else:
        return date[0:5]+str(month-1)+'/28'
    
def findSecondComma(string):
    c1 = string.find(',')
    c2 = 1+c1+string[c1+1:].find(',')
    return c2+1

# num -> str
def colorCode(depth):
    """Takes in the depth of an earthquake and
    returns a color in order to color-code
    earthquakes of different magnitudes."""
    if (depth<34):
        return 'orange'
    elif (depth<71):
        return 'yellow'
    elif (depth<151):
        return 'green'
    elif (depth<301):
        return 'blue'
    elif (depth<501):
        return 'purple'
    else:
        return 'red'

import turtle

def plotEarthquakeData(date1,date2):
    myBg = turtle.Screen()
    myBg.setworldcoordinates(-180,-90,180,90)
    myBg.bgpic('worldmap.jpg')
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    myTurtle.up()
    myTurtle.speed(0)
    data = parseEarthquakeData(date1,date2)
    dots = 0
    for item in data:
        myTurtle.goto(float(item[1]),float(item[0]))
        try:
            myTurtle.dot(float(item[2])*4,colorCode(float(item[3])))
        except:
            pass
        dots += 1
    a = input('Press enter to exit')
    myTurtle.clear()
