import json 

strings = [""]*5
strings[1] += "0,emotion,0\n"
strings[0] += "0,paragraph,0\n"
strings[2] += "0,image,0\n"
strings[4] += "0,phoneme,m\n"

prevPhoneme = "na"

def addPhoneme(p, t):
    global prevPhoneme
    global f
    if p != prevPhoneme:
        strings[4] += (str.format('{0:.3f}', t)+",phoneme,"+p+"\n")
    prevPhoneme = p

mouthList = [["aa","a"],["ae","a"],["ah","a"],["ao","a"],["aw","au"],
["ay","ay"],["b","m"],["ch","t"],["d","t"],["dh","t"],
["eh","a"],["er","u"],["ey","ay"],["f","f"],["g","t"],
["hh","y"],["ih","a"],["iy","ay"],["jh","t"],["k","t"],
["l","y"],["m","m"],["n","t"],["ng","t"],["ow","au"],
["oy","ua"],["p","m"],["r","u"],["s","t"],["sh","t"],
["t","t"],["th","t"],["uh","u"],["uw","u"],["v","f"],
["w","u"],["y","y"],["z","t"],["zh","t"],
["oov","m"]] # For unknown phonemes, the stick figure will just have a closed mouth ("mmm")


###### The following for loop just converts the 'mouthList' nested list into a simple dictionary with the same information.
mouths = {}
for x in mouthList:
    mouths[x[0]] = x[1]

INPUT_FILE = "transcript_raw/raw_transcript.json"

f = open(INPUT_FILE,"r+")
fileData = f.read()
f.close()

data = json.loads(fileData)
WORD_COUNT = len(data['words'])

word = data['words']
for i in range(WORD_COUNT):
    word = data['words'][i]
    if "start" not in word:
        continue
    wordString = word['word']
    timeStart = word['start']
    timeAt = timeStart
    #print(word)
    #print(wordString)
    phones = word["phones"]
    for phone in phones:
        timeAt += phone["duration"]
        phoneString = phone["phone"]
        if phoneString == "sil":
            truePhone = "m"
        else:
            truePhone = mouths[phoneString[:phoneString.index("_")]]
        print(timeAt-phone["duration"])
        if len(truePhone) == 2:
            addPhoneme(truePhone[0], timeAt-phone["duration"])
            addPhoneme(truePhone[1], timeAt-phone["duration"]*0.5)
        else:
            addPhoneme(truePhone, timeAt-phone["duration"])

print(strings[4])

