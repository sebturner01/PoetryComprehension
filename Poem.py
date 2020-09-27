"""
Authors: Damian Armijo and Sebastian Turner
Date: 09/23/19

This class reperesents a poem and the fundemental components contained within it.
"""

#----------------
# Init 
#----------------
from Levenshtein import distance as dis
#----------------
# Class
#----------------

class Poem:
"""Initializes a given Poem as a class."""
=======
    def __init__(self, attributes: dict, textAuthor = "", text = "", PublishedYear = 0):
        self.author = textAuthor
        self.content = text
        self.year = PublishedYear
        self.attributes = attributes

    def retrieveAttribute(attribute):
      """Given the name of an attribute as a string this program will return 
        the value assosciated with the key attribute 
        
        Inputs:
            attribute - a string that is the key to a value in attribues

        Outputs:
            Returns the given attribute. If the attribute is not found then None will be
            returned and any attributes that are a maximum Levenstien distance 2
        """
        attr = self.attributes.get(attribute)
        return attr if attr else fuzzyKeySearch
   
    def fuzzyKeySearch(self, key):
        """This function is to be called by retrieveAttribute in the case that the given
        attribute was misspelled. Using a levenstien distance of 1 this program will then
        search the attributes dictionary for the fuzzy match.
        Output:
            Returns None if a fuzzy match cannot be found. If there is more than one potential match then all appropriate options will be printed out for the user to select.        
        """
        print(f'{key} is not an attribute did you mean?\n')
        for attr in self.attributes:
            if dis(key, attr) < 2:
                print(attr)
