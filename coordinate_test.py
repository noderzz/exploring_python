import numpy as np

f = open("coordinates.csv","r+")
mouthCoordinatesStr = f.read().split("\n")
f.close()

#print(mouthCoordinatesStr)
#print(len(mouthCoordinatesStr))

#parts = mouthCoordinatesStr[1].split(',')
#print(parts)

POSE_COUNT = 30
MOUTH_COOR = np.zeros((POSE_COUNT,5))
for i in range(len(mouthCoordinatesStr)):
    parts = mouthCoordinatesStr[i].split(",")
    for j in range(5):
        MOUTH_COOR[i,j] = float(parts[j])
print(MOUTH_COOR[29])
print(parts)

