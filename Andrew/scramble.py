# A little tutorial script that hopefully helps understand some of
# What is a variable?
# What is an import?
# What is a function, and how do they work?
# Types matter, even in python
# Very simple error handling and debugging
# Basic for loop

# **** See `scrambleWithNotes.py` for a line-by-line explanation ****

import random
from pprint import pprint

def ScrambleMessage(message):
    if type(message) == str:
        characterList = list(message)
        random.shuffle(characterList)
        scrambled = ''.join(characterList)

        return scrambled 

    return ''  # gonna return an empty string as a return.

input = "Nikolas Drakulovic"
numScrambles = 10

listOfScrambles = []    

for i in range(numScrambles):
    print("Scrambling " + str(i) + " time(s)...")
    listOfScrambles.append(ScrambleMessage(input))

print()
print(input + " scrambled in " + str(numScrambles) + " different ways:")
pprint(listOfScrambles)