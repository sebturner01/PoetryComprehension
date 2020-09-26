"""
Authors: Damian Armijo and Sebastian Turner
Date: 09/23/20

This file has the functions which can take text and can turn it into a poem.
"""

# ----------------
# Init
# ----------------
import Poem as po
import os.path
from os import path
import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
import string
from collections import defaultdict, OrderedDict
import operator


def readFromTextFile(fileString):
    """ This function reads the file from the provided string and returns the read string """

    if path.exists(fileString):

        f = open(fileString, "r", encoding="utf-8")
        return f.read()

    return None


def lineCount(poemString):
    """ This function returns number of lines from the poem string. """
    lines = poemString.splitlines()
    if "" in lines:
        lines.remove("")
    return len(lines)


def wordCount(poemString):
    """ This function returns number of words from the poem string. """
    return len(poemString.split())


def makePoem(poemString, author="", publishedDate=-1):
    """This function takes in the string poem and gets it's attributes,
    It also takes in the author's name, and the date of publication.
    It returns a Poem object containing which is made from the given info."""

    attributes = {
        "WordCount": wordCount(poemString),
        "lineCount": lineCount(poemString),
    }

    return po.Poem(attributes, author, poemString, publishedDate)


class PoemAnalyzer:
    def alliterationInPoem(poem):
        """Prints out the alliteration from a poem, broken up by lines.
        https://stackoverflowfinding-alliterative-word-sequences-with-python"""
        poemLines = poem.content.splitlines()

        # Get the English alphabet as a list of letters
        letters = [letter for letter in string.ascii_lowercase]

        # Here we add some extra phonemes that are distinguishable in text.
        # ('sailboat' and 'shark' don't alliterate, for instance)
        # Digraphs go first as we need to try matching these before the individual letters,
        # and break out if found.
        sounds = ["ch", "ph", "sh", "th"] + letters

        # Use NLTK's built in stopwords and add "'s" to them
        stopwords = nltk.corpus.stopwords.words("english") + [
            "'s"
        ]  # add extra stopwords here
        stopwords = set(stopwords)  # sets are MUCH faster to process

        for t in poemLines:

            sents = sent_tokenize(t)
            alliterating_sents = defaultdict(list)
            for sent in sents:
                tokenized_sent = word_tokenize(sent)

                # Create list of alliterating word sequences
                alliterating_words = []
                previous_initial_sound = ""
                for word in tokenized_sent:
                    for sound in sounds:
                        if word.lower().startswith(
                            sound
                        ):  # only lowercasing when comparing retains original case
                            initial_sound = sound
                            if initial_sound == previous_initial_sound:
                                if len(alliterating_words) > 0:
                                    if (
                                        previous_word == alliterating_words[-1]
                                    ):  # prevents duplication in chains of more than 2 alliterations, but assumes repetition is not alliteration)
                                        alliterating_words.append(word)
                                    else:
                                        alliterating_words.append(previous_word)
                                        alliterating_words.append(word)
                                else:
                                    alliterating_words.append(previous_word)
                                    alliterating_words.append(word)
                            break  # Allows us to treat sh/s distinctly

                    # This needs to be at the end of the loop
                    # It sets us up for the next iteration
                    if (
                        word not in stopwords
                    ):  # ignores stopwords for the purpose of determining alliteration
                        previous_initial_sound = initial_sound
                        previous_word = word

                alliterating_sents[len(alliterating_words)].append(sent)

            sorted_alliterating_sents = OrderedDict(
                sorted(
                    alliterating_sents.items(), key=operator.itemgetter(0), reverse=True
                )
            )

            # OUTPUT
            print("A sorted ordered dict of sentences by number of alliterations:")
            print(sorted_alliterating_sents)
            print("-" * 15)


# TODO -----------------
# TODO  Make return appropriate For data usage.
# TODO  Test
# TODO  Remove some unecessary code
# TODO ------------------
