# A little tutorial script that hopefully helps understand some of
# What is a variable?
# What is an import?
# What is a function, and how do they work?
# Types matter, even in python
# Very simple error handling and debugging
# Basic for loop

import random   # imports package `random` which will contain a bunch of functions
                # each of these functions are callable by typing 
                # random.FUNCTIONNAME(parameters)

from pprint import pprint   # Another way to import functions from a module. here, what I'm doing 
                            # is only importing the function `pprint` from the module `pprint`
                            # which lets me call it by typing
                            # pprint(thingsToPrint)
                            # rather than
                            # pprint.pprint(thingsToPrint)
                            # this method is useful when you don't want to import the entire module
                            # **** IF YOU DON'T HAVE THIS PACKAGE, THEN TYPE "pip install pprint" INTO THE COMMAND LINE!!!!!! ****

def ScrambleMessage(message):   # define a variable called `ScrambleMessage` - a function which takes 1 parameter `message`

    if type(message) == str:    # This if statement checks if `message` is a string type. If it is, then run the below code

        characterList = list(message)   # takes `message and converts it into a string of characters, i.e.
                                        # message == "Nikolas Drakulovic"
                                        # characterList == ['N', 'i', 'k', 'o', 'l', 'a', 's', ' ', 'D', 'r', 'a', 'k', 'u', 'l', 'o', 'v', 'i', 'c']

        random.shuffle(characterList)   # using the `shuffle` function from module `random` to randomize the order of the characters in `characterList`

        scrambled = ''.join(characterList)  # Maybe confusing, but here's what's happening:
                                            # the `join` function takes a string, or a list of characters (in this case) and 
                                            # joins them with the string it's being called on. Here, I'm calling `join` on the literal of an empty string
                                            # and passing in `characterList` to join all those characters together.
                                            # simply put, this makes the character list back into a string.
                                            # --
                                            # a more conventional use of this would be:
                                            # andrewDaly = "Andrew ".join("Daly")
                                            # and now andrewDaly is equal to "Andrew Daly", as we told the literal "Andrew " to join with "Daly"

        return scrambled    # return the scrambled string. The function ends, and the below error handling code does not run
    
    return ''   # This is basically the `else` to the above if statement. if `message` isn't a string, I'm just
                # gonna return an empty string as a return.


# Try me out. Here I'm declaring two variables, 
# `input` which is a string, and 
# `numScrambles` which is the number of times to scramble that string
input = "Nikolas Drakulovic"
numScrambles = 10

listOfScrambles = []    # Declaring an empty list. we're going to scramble `input`
                        # and, one at a time, add the result of that scramble to this list

for i in range(numScrambles):   # Basic for loop structure. `i` is the loop number, and range(num) is how many times to loop
    print("Scrambling " + str(i) + " time(s)...")   # Prints the progress of building this list
    listOfScrambles.append(ScrambleMessage(input))  # The meat of the script, this says "call the ScrambleMessage function using the
                                                    # input we defined above, then add this result to the `listOfScrambles` list using the
                                                    # `append` function"

print() # Prints an empty line in the command window
print(input + " scrambled in " + str(numScrambles) + " different ways:")    # Read the output this makes sense I think
pprint(listOfScrambles) # What the fuck is pprint? good question! it's just a package I like to use that formats
                        # console messages better than the built-in `print`. Try it out and see the difference!
