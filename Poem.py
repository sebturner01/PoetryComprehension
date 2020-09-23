"""
Authors: Damian Armijo and Sebastian Turner
Date: 09/23/19

This class reperesents a poem and the fundemental components contained within it.
"""

#----------------
# Init 
#----------------
import python-Levenshtein
import fuzzywuzzy
#----------------
# Class
#----------------

class Poem:
    def __init__(self, textAuthor = "", text = "", PublishedYear : int = 0, attributes):
        """Initializes a given Poem as a class."""
        self.author = textAuthor
        self.content = text
        self.year = PublishedYear
        self.attributes = attributes

    def retrieveAttribute(attribute):
        """Given the name of an attribute as a string this program will return"""
        if not self.attributes.get(attribute):

    def fuzzyKeySearch(key):
        """This function is to be called by retrieveAttribute in the case that the given
        attribute was misspelled. Using a levenstien distance of 1 this program will then
        search the attributes dictionary for the fuzzy match
        
        Input:
            key - a string that corresponds to a value in "attributes"

        Output:
            Returns None if a fuzzy match cannot be found. If there is more than one potential match then both options will be printed out for the user to select.        
        """
        


    