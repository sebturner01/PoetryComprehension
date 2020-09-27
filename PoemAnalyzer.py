# Authors: Damian Armijo and Sebastian Turner 
# Date: 09/27/20
# All fucntions that are not getPoemPhones require getPoemPhones to run and this 
# function to 

#-----------------
# Init
#-----------------
import pronouncing
import Poem 
#-----------------
# Functions
#-----------------

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
    words = poem.text.word_tokenize()
    for w in words:
        pronouncing.phones_for_word()
    poem.attributes['phones'] = phones

def findAllRhymes(poem: Poem):
    #TODO: figure out performance issues with rhyming
    #   perhaps find a most common words list and store in memory
    #   database?
    return

def findSingleRhyme(poem):
    return
    


    sin
deafl findAlliteration(poem):
    """Adds a poems alliterations to its attributes
        
        Inputs:
            poem - an instance of a poem class.

        Outputs
    
    """
        phones = poem.attributes['phones']
        
        s PoemAnalyzer:
    def alliterationInPoem(poem):
        """Prints out the alliteration from a poem, broken up by lines.




        https://stackoverflowfinding-alliterative-word-sequences-with-python"""

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
    
        t in poemLines:
    
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
                                    
                                alliterating_words.append(previous_word)
                                    terating_words.append(word)
                                    ows us to treat sh/s distinctly
                            
                                be at the end of the loop
                                for the next iteration
                        
                        word not in stopwords
                ):  # ignores stopwords for the purpose of determining alliteration
                    previous_initial_sound = initial_sound
                    previous_word = word
                    
                terating_sents[len(alliterating_words)].append(sent)
                    
                    erating_sents = OrderedDict(
                sorted(
                alliterating_sents.items(), key=operator.itemgetter(0), reverse=True
                )
        )
            
                
            t("A sorted ordered dict of sentences by number of alliterations:")
        print(sorted_alliterating_sents)
            print("-" * 15)                                