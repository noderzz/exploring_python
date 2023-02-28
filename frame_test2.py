import numpy as np

f = open("phoneme_list.csv","r+")
scheduleLines = f.read().split("\n")
f.close()

PARTS_COUNT = 5
FRAME_RATE = 30
phonemeTimeline = []

def timestepToFrames(timestep):
    return max(0,int(timestep*FRAME_RATE-2))

for i in range(len(scheduleLines)):
    parts = scheduleLines[i].split(",")
    timestamp = float(parts[0])
    framestamp = timestepToFrames(timestamp)
    phoneme = parts[2]
    phonemeTimeline.append([phoneme,framestamp])

LAST_FRAME = int(phonemeTimeline[-1][-1]) + 1
phonemeTimeline.append(["end",LAST_FRAME])
print(phonemeTimeline)