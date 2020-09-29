# Author: Damian Armijo and Sebastian Turner 
# Date: 09/26/20
# This is the testing module for the Poetry comprehension package. 
# As of (09/20) it will only consist of unit tests.
import Poem
import Parser
import PoemAnalyzer


name = "TestResults.txt"

if __name__ == "__main__":

    #Creates a testing results file
    with open(name, 'w') as f:
        pass

    poems = []
    
    """Input Testing""" 
    #Testing with non-existentFile
    poem1 = readFromTextFile("doesNotExist.txt")
    poems.append(poem)

    #Testing with empty string
    poem = readFromTextFile("")
    poems.append(poem)
    
    #Testing with the Haiku
    poem = readFromTextFile("haiku.txt")
    poems.append(poem)

    #Testing with a sonnet
    poem = readFromTextFile("sonnet.txt")
    poems.append(poem)
    
    #Testing with a longer text
    poem = readFromTextFile("GitaChp1.txt")
    poems.append(poem)

    """Testing Parser, Poem class and PoemAnalyzer Funcitons"""

    # Prints a poem's text and attributes to the testing file

    for p in poems:
        PoemAnalyzer.getPoemPhones(p)
        PoemAnalyzer.findAlliteration(p)
        with open(name, 'a') as f:
            newPoem = makePoem(p)
            f.write(p)
            for attr in newPoem.attributes:
                f.write(attr)
                




