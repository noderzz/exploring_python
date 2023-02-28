PARTS_COUNT = 5
CACHES = [[None,None]]*PARTS_COUNT
FRAME_CACHES = {}
indicesOn = [-1]*(PARTS_COUNT-1)

#print(CACHES)
#print(indicesOn)

schedules = [None]*PARTS_COUNT
#schedules = [1, 2, 3, 4]

f = open("coordinates.csv","r+")
scheduleLines = f.read().split("\nSECTION\n")
f.close()

for i in range(len(scheduleLines)):
    schedules[i] = scheduleLines[i].split("\n")
    if i == 4:
        schedules[i] = schedules[i][0:-1]

timestamp = float(schedules)

FRAME_RATE = 30
def timestepToFrames(timestep):
    return max(0,int(timestep*FRAME_RATE-2))

print(schedules)

lastParts = schedules[-1][-2].split(",")
lastTimestamp = float(lastParts[0])
#FRAME_COUNT = timestepToFrames(lastTimestamp+1)

#for frame in range(0,FRAME_COUNT):
#    for p in range(PARTS_COUNT-1):
#        frameOfNext = frameOf(p,1)
#        if frameOfNext >= 0 and frame >= frameOfNext:
#            indicesOn[p] += 1