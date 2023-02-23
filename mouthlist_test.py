mouthList = [["aa","a"],["ae","a"],["ah","a"],["ao","a"],["aw","au"],
["ay","ay"],["b","m"],["ch","t"],["d","t"],["dh","t"],
["eh","a"],["er","u"],["ey","ay"],["f","f"],["g","t"],
["hh","y"],["ih","a"],["iy","ay"],["jh","t"],["k","t"],
["l","y"],["m","m"],["n","t"],["ng","t"],["ow","au"],
["oy","ua"],["p","m"],["r","u"],["s","t"],["sh","t"],
["t","t"],["th","t"],["uh","u"],["uw","u"],["v","f"],
["w","u"],["y","y"],["z","t"],["zh","t"],
["oov","m"]] # For unknown phonemes, the stick figure will just have a closed mouth ("mmm")

mouths = {}
for x in mouthList:
    mouths[x[0]] = x[1]

#print(mouthList)
print(mouths)

