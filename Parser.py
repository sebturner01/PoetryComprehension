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
