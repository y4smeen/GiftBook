import urllib2
import readFile
from datetime import datetime

url = "http://datamine.mta.info/files/k38dkwh992dk/gtfs"
googleKey = "AIzaSyAsvu3vJPPUS-VZM3bb7-KII5YyjmvyhPk"

def findTrain(origin, destination):
    finalList = readFile.fin()
    possiblities = []
    for each in finalList:
        if origin == each[1] or destination == each[1]:
            possiblities.append(each)
    print possiblities
    narrowed = []
    x = len(possiblities)-1
    while x > 1:
        if possiblities[x][1] != possiblities[x-1][1]:
            if possiblities[x][0] == possiblities[x-1][0]:
                narrowed.append(possiblities[x])
                narrowed.append(possiblities[x-1])
        x = x-2

    string = ""
    for each in narrowed:
        string = string + each[0] + " train at " + each[1] + " at " + each[2] + "<br>"

    if len(narrowed) == 0:
        return "There are no trains connecting your two destinations. Please locate other subway stations and search again."
    else:
        return "Congratulations! There is/are " + str(len(narrowed)/2) + " trains connecting your two destinations. <br>They are as follows:<br>" + string
