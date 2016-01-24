file = open("static/stops.txt")

stops = file.read().split("\n")
names = {}
for stop in stops[1:-1]:
  temp = stop.split(",")
  if not temp[2] in names:
      names[temp[0]] = temp[2]

#for name in names:
#    print name + " " + names[name] + "\n"

#print "<select>"
#for name in names:
#    print "<option value='%s'> %s </option>" % (name, name)
#print "</select>"



stopTime = open("static/stop_times.txt")

lines = stopTime.read().split("\n")
ids = {}
subway = {}
for time in lines[1:-1]:
    temp = time.split(",")
    ids[temp[3]] = temp[1]
    subway[temp[3]] = temp[0]
#for i in ids:
#    print ids[i] + " " + names[i] + "\n"




trips = open("static/trips.txt")

line = trips.read().split("\n")
trains = {}
for each in line[1:-1]:
    temp = each.split(",")
    trains[temp[2]] = temp[0]


def fin():
    final = []
    for i in ids:
        temp = []
        temp.append(trains[subway[i]]) #train
        temp.append(names[i]) #station
        temp.append(ids[i]) #time
        final.append(temp)
    return final
