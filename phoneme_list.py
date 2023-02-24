import json 

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
    #print(word)
    print(wordString)


