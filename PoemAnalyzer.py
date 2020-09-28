# Authors: Damian Armijo and Sebastian Turner
# Date: 09/27/20
# All fucntions that are not getPoemPhones require getPoemPhones to run and this
# function to

# -----------------
# Init
# -----------------
import pronouncing
import Poem
import nltk

# -----------------
# Functions
# -----------------


def getPoemPhones(poem: Poem):
    """Adds a poems pronuciation to its attributes

    Inputs:
        poem - an instance of a poem class.

    Outputs:
        No direct output. However, the instance of the poem class that was passed
        to this function does gain a "phones" attribute that contains the ARPAbet
        pronunciation of each word in the poem.

    """
    # TODO: Replace with basic CMUdict lookup
    phones = []
    words = nltk.tokenize.word_tokenize(poem.content)
    for w in words:
        phones.append(pronouncing.phones_for_word(w))
    poem.attributes["phones"] = phones


def findAllRhymes(poem: Poem):
    # TODO: figure out performance issues with rhyming
    #   perhaps find a most common words list and store in memory
    #   database?
    return


def findSingleRhyme(poem):
    return


def findAlliteration(poem):
    """Adds a poems alliterations to its attributes

    Inputs:
        poem - an instance of a poem class.

    Outputs:
        allitDict - a dictionary of alliterations in the poem
            ex:{alliteration starting word #: ending word #, ...}

    """

    phones = poem.attributes["phones"]  # [['HH AH0 L OW1', 'HH EH0 L OW1',...],...]

    listOfFrontSounds = getFrontSounds(phones)
    allitDict = dictFromFrontSounds(listOfFrontSounds)

    return allitDict


def dictFromFrontSounds(listOfFrontSounds):
    """Function used by findAlliteration() which makes a dictionary of alliteration
        from a list of front sounds.

    Inputs:
        listOfFrontSounds - a list of starting sounds of

    Outputs:
        allitDict - a dictionary of alliterations in the poem {alliteration starting
            word #: ending word #, ...}

    """
    allitDict = dict()
    frontOfList = listOfFrontSounds[0]
    foundSame = False
    count = 0

    for i in range(1, len(listOfFrontSounds)):
        newList = listOfFrontSounds[i]
        foundSame = False
        for x in newList:
            if frontOfList.count(x) > 0:
                foundSame = True
                break

        if foundSame:
            count += 1
        if not foundSame:
            if count > 0:
                allitDict[i - count] = i
            count = 0
        frontOfList = newList
    return allitDict


def getFrontSounds(phones):
    """Function used by findAlliteration() which makes a list of front sounds
        from a list of word sounds.

    Inputs:
        phones - a list of word sounds.

    Outputs:
        listOfFrontSounds - a list of starting sounds of words.

    """
    listOfFrontSounds = []
    for words in phones:
        tempSet = set()
        for sounds in words:
            firstSound = sounds.split()[0]
            tempSet.add(firstSound)
        listOfFrontSounds.append(list(tempSet))
    listOfFrontSounds = [x for x in listOfFrontSounds if x != []]
    return listOfFrontSounds
