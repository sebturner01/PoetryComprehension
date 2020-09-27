    # Author: Damian Armijo and Sebastian Turner 
# Date: 09/26/20
# This is the testing module for the Poetry comprehension package. 
# As of (09/20) it will only consist of unit tests.

import Parser *

if __name__ == "__main__":

    """Input Testing""" 
    #Should print None
    poem = readFromTextFile("doesNotExist.txt")
    print(poem)

    #Should print None
    poem = readFromTextFile("")
    print(poem)
    
    poem = readFromTextFile("haiku.txt")
    print(poem) 

    poem = readFromTextFile("GitaChp1")

    





