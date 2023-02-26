PARTS_COUNT = 5
CACHES = [[None,None]]*PARTS_COUNT
FRAME_CACHES = {}
indicesOn = [-1]*(PARTS_COUNT-1)

#print(CACHES)
#print(indicesOn)

schedules = [1, 2, 3, 4]

timestamp = float(schedules)

FRAME_RATE = 30
def timestepToFrames(timestep):
    return max(0,int(timestep*FRAME_RATE-2))

print(schedules)

#FRAME_COUNT = timestepToFrames(lastTimestamp+1)

#for frame in range(0,FRAME_COUNT):