    # Author: Damian Armijo and Sebastian Turner 
# Date: 09/26/20
# This is the testing module for the Poetry comprehension package. 
# As of (09/20) it will only consist of unit tests.

from Parser import readFromTextFile
from parser import makePoem


name = "TestResults.txt"

if __name__ == "__main__":

    #Creates a testing results file
    with open(name, 'w') as f:
        pass

    poems = []
    
    """Input Testing""" 
    #Should print None
    poem1 = readFromTextFile("doesNotExist.txt")
    poems.append(poem)

    #Should print None
    poem = readFromTextFile("")
    poems.append(poem)
    
    poem = readFromTextFile("haiku.txt")
    poems.append(poem)

    poem = readFromTextFile("GitaChp1.txt")
    poems.append(poem)

   
    """Testing Parser and Poem class Funcitons"""
    
    with open(name, 'a') as f:
        for p in poems:
            newPoem = makePoem(p)
            f.write(p)
            for attr in newPoem.attributes:
                f.write(attr)
                




