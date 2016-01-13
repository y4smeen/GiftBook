file = open("static/stops.txt")

stops = file.read().split("\n")
names = []
for stop in stops[1:-1]:
  temp = stop.split(",")
  if not temp[2] in names:
      names.append(temp[2])

print "<select>"
for name in names:
    print "<option value='%s'> %s </option>" % (name, name)
print "</select>"
