f = open("coordinates.csv","r+")
scheduleLines = f.read().split("\nSECTION\n")
f.close()

PARTS_COUNT = 5
schedules = [None]*PARTS_COUNT

for i in range(PARTS_COUNT):
    schedules[i] = scheduleLines[0].split("\n") #Error because scheduleLines is one list item long (0)
    if i == 4:
        schedules[i] = schedules[i][0:-1]

print(schedules)

#for i in scheduleLines:
#    print(i.split("\n"))

#print(schedules[4])
#for i in range(len(schedules[4])):