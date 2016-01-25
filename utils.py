import urllib2
import readFile
from datetime import datetime

from google.transit import gtfs_realtime_pb2
import urllib

import os.path
#from google.transit import gtfs_realtime_pb2
import unittest
import nyct_subway_pb2

url = "http://datamine.mta.info/files/k38dkwh992dk/gtfs"
googleKey = "AIzaSyAsvu3vJPPUS-VZM3bb7-KII5YyjmvyhPk"
mtaKey = "9193038a235910373a5db2c3e6e954fa"
FEED_ID = 2
train = 0

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

def tripUpdate():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urllib.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
    feed.ParseFromString(response.read())
    for item in feed.entity:
        if item.HasField('trip_update'):
        print item.trip_update

def get_realtime_subway(train, feed_id = FEED_ID, key = API_KEY):
    feed = gtfs_realtime_pb2.FeedMessage()
    url = 'http://datamine.mta.info/mta_esi.php?key=%s&feed_id=%s' % (key, feed_id)
    response = urllib2.urlopen(url)
    feed.ParseFromString(response.read())
    arrival_times = []
    for item in feed.entity:
        for stop_time_update in item.trip_update.stop_time_update:
            if stop_time_update.stop_id == train:
                arrival_times.append(datetime.datetime.fromtimestamp(stop_time_update.arrival.time))
    return sorted(arrival_times)
