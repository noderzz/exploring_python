import json 

INPUT_FILE = "transcript_raw/raw_transcript.json"

f = open(INPUT_FILE,"r+")
fileData = f.read()
f.close()

data = json.loads(fileData)
word = data['words'][2]
#subsection = word['phones']

print(word['phones'])