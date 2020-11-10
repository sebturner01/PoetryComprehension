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
import copy
import re

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
    words = sanitizeWords(poem.content)
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


def findEndRhyme(poem: Poem):
    """Adds a poems end Rhymes to its attributes

    Inputs:
        poem - an instance of a poem class.

    Outputs:
        endRhymes - a dictionary of end rhymes in the poem
            {(word,line #): [(word,line #), ...]}

    """
    # TODO: make more efficient
    # make more pythonic
    endingWords = enumerate(getEndWords(poem.content))
    endRhymes = {}
    for lineNum, word in endingWords:
        tempSet = set()
        endingWords2 = copy.deepcopy(endingWords)
        for lineNum2, word2 in endingWords2:
            if word2 in pronouncing.rhymes(word):
                tempSet.add((lineNum2, word2))
        endRhymes[(lineNum, word)] = list(tempSet)
    poem.attributes["endRhymes"] = endRhymes


def getEndWords(poemString):

    endingWordsList = []
    splitPoem = poemString.splitlines()

    for line in splitPoem:
        words = sanitizeWords(line)
        if len(words) > 0:
            endingWordsList.append(words[-1])
    return endingWordsList


def sanitizeWords(content):
    """Removes symbols from the words from the content of a poem.

    Inputs:
        content - a string, of the content of a Poem.

    Outputs:
        words - a list of nltk tokenized words from the content
             ['An','example',...]
    """
    # TODO: check to make sure it works to the full extent.
    # Maybe store in the poem.
    words = nltk.tokenize.word_tokenize(content)
    words = list(
        filter(lambda a: len(a) > 0 and a[0].isalpha(), words)
    )  # Remove symbols from list
    return words


def findAlliteration(poem: Poem):
    """Adds a poems alliterations to its attributes

    Inputs:
        poem - an instance of a poem class.

    Outputs:
        allitDict - a dictionary of alliterations in the poem
            {alliteration starting word #: ending word #, ...}

    """
    # TODO: Test fully to see if works correctly
    #   Test speed
    phones = poem.attributes["phones"]  # [['HH AH0 L OW1', 'HH EH0 L OW1',...],...]
    listOfFrontSounds = getFrontSounds(phones)
    allitDict = dictFromFrontSounds(listOfFrontSounds)
    poem.attributes["alliteration"] = allitDict
    return allitDict


def dictFromFrontSounds(listOfFrontSounds):
    """Function used by findAlliteration() which makes a dictionary of alliteration
        from a list of front sounds.

    Inputs:
        listOfFrontSounds - a list of starting sounds of

    Outputs:
        allitDict - a dictionary of alliterations in the poem
            {alliteration starting word #: ending word #, ...}

    """
    allitDict = dict()
    frontOfList = listOfFrontSounds[0]
    foundSame = False
    count = 0
    for index, sound in enumerate(listOfFrontSounds[1:], 1):
        newList = sound
        foundSame = False
        for x in newList:
            if frontOfList.count(x) > 0:
                foundSame = True
                break

        if foundSame:
            count += 1
        elif count > 0:
            allitDict[index - (count + 1)] = index - 1
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
    return fixNotInCMU(listOfFrontSounds)


def fixNotInCMU(listOfFrontSounds):
    """Function used by getFrontSounds() which adds placeholders ('1','2') to listOfFrontSounds
        for words not in CMU dictionary ***THIS SHOULD BE CHANGED LATER***.

    Inputs:
        listOfFrontSounds - a list of starting sounds of words.

    Outputs:
        listOfFrontSounds - a list of starting sounds of words(adjusted).

    """
    # TODO: add words to dictionary! Not '1', '2' placeholder shenanigans
    switcher = True
    for sound in listOfFrontSounds:
        if sound:
            if switcher:
                sound = ["1"]
            else:
                sound = ["2"]
            switcher = not switcher

    return listOfFrontSounds


def getSimilies(poem: Poem):
    """Adds a poems similies to its attributes

    Inputs:
        poem - an instance of a poem class.

    Outputs:
        No direct output. However, the instance of the poem class that was passed
        to this function does gain a "similies" attribute that contains the regex
        defined, group of similies in the poem.

    """
    # TODO: break this regex, or find it magically works.
    words = poem.content
    similies = re.search(r"(?i)\blike (a|an|the)\b|as \w{1,} as (a|an|the)", str(words))
    poem.attributes["similies"] = similies
=======


def getSyllableCount(poem: Poem):
    """Adds a poems similies to its attributes

    Inputs:
        poem - an instance of a poem class.

    Outputs:
        No direct output. However, the instance of the poem class that was passed
        to this function does gain a "similies" attribute that contains the regex
        defined, group of similies in the poem.

    """
    # TODO: check validity
    flatten = lambda l: [
        item for sublist in l for item in sublist
    ]  # this flattens list of lists to list

    phones = poem.attributes["phones"]
    phones = flatten(removeSyllableDuplicates(phones))
    poem.attributes["syllableCount"] = sum(
        [pronouncing.syllable_count(p) for p in phones]
    )


def removeSyllableDuplicates(syllableList):
    """This is a helper function that removes duplicate phonetic breakups
    that comes from pronouncing library.
    Ex: [['S N OW1'], ['B IY1', 'B IY0']] --> [['S N OW1'], ['B IY1']]
    """
    plist = []
    for x in syllableList:
        if len(x) > 1:
            plist.append(x[0])
        else:
            plist.append(x)
    return plist


def getStanzaCount(poem: Poem):
    """Adds a poems stanzaCount to its attributes

    Inputs:
        poem - an instance of a poem class.

    Outputs:
        No direct output. However, the instance of the poem class that was passed
        to this function does gain a "stanzaCount" attribute that contains the
        poems stanza count.

    """
    stanzaCount = poem.content.count("\n\n") + 1
    poem.attributes["stanzaCount"] = stanzaCount
