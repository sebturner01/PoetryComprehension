# Authors: Damian Armijo and Sebastian Turner
# Date: 09/27/20
# This file has the functions which can analyze poems, and csv poem data.

# -----------------
# Init
# -----------------
from sklearn.decomposition import IncrementalPCA  # inital reduction
from sklearn.manifold import TSNE  # final reduction
import numpy as np  # array handling
import csv
import copy
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action="ignore")
import Parser as pars
import gensim  # For modeling
from gensim.models import Word2Vec

# -----------------
# Functions
# -----------------


def dataFromCSV(fileName):
    """Adds a poems pronuciation to its attributes

    Inputs:
        fileName - a string with the csv file name.

    Outputs:
        dataSet - a dictionary of data from csv file
            key - the author
            value - a list of all values from that author.
            ex: {'Charles Bukowski':
                    [['27', 'Charles Bukowski', '8 count',
                    '49699', "from my bed\nI watch..."],
                    ...]
                ...}
    """
    dataSet = {}
    with open(fileName, encoding="utf8") as csvfile:

        readCSV = csv.reader(csvfile, delimiter=",")
        csvList = list(readCSV)
        csvList.sort(key=lambda x: x[1])  # order the list by author
        author = ""
        tempList = []
        for row in csvList:
            if not tempList:
                author = row[1]
            if author != row[1] and len(tempList) > 0:
                tempList.append(row)
                dataSet[author] = copy.deepcopy(tempList)
                author = row[1]
                tempList = []
            tempList.append(row)

    return dataSet


def modelDataFromText(text):
    """Turns text into data for word2vec modeling.

    Inputs:
        text - a string which is the poem, or multiple poems text.

    Outputs:
        data - a list of tokenized "data" (words) that can be used for modeling.

    """
    sent = text
    sent.replace("\n", " ")

    data = []

    # iterate through each sentence in the file
    for i in sent_tokenize(sent):
        temp = []

        # tokenize the sentence into words
        for j in word_tokenize(i):
            temp.append(j.lower())

        data.append(temp)

    return data


def textsFromPoemList(poemList):
    """Gets text from a list of poems for data processing.

    Inputs:
        poemList - a list of Poems.

    Outputs:
        texts - a string of the poems' content.

    """
    texts = ""
    for poem in poemList:
        texts += poem.content
    return texts


def poemListFromCSVData(csvData):
    """Gets a list of Poems from properly organized CSV data.

    Inputs:
        csvData - a list of data from the csvdata, a grouping
            of poems based on whatever you decide(author,type,etc...).

    Outputs:
        poemList - a list of poems made from the CSV data provided.

    """
    poemList = []
    for poem in csvData:
        poemList.append(pars.makePoem(poem[4], poem[1], -1))
    return poemList


def cbowModel(modelData):
    """Gets a word2vec model based on CBOW

    Inputs:
        modelData - a list of strings(words) , this is "data" to be modelled.

    Outputs:
        a gensim CBOW model from word2vec

    """
    # Create CBOW model
    return gensim.models.Word2Vec(modelData, min_count=1, size=200, window=5)


def gramModel(modelData):
    """Gets a word2vec model based on Skip Gram

    Inputs:
        modelData - a list of strings(words) , this is "data" to be modelled.

    Outputs:
        a gensim Skip Gram model from word2vec

    """
    # Create Skip Gram model
    return gensim.models.Word2Vec(modelData, min_count=1, size=200, window=5, sg=1)


def plotModel(model, fileLabel="PCA_plot"):
    """Plots a model in a notebook, and also in a pdf.

    Inputs:
        model - a word2vec model.
        fileLabel - a label for the PCA plot.

    Outputs:
        No direct output, but it does create a pdf file of the plot.

    """
    x_vals, y_vals, labels = reduce_dimensions(model)

    try:
        get_ipython()
    except Exception:
        plot_function = plot_with_matplotlib
    else:
        plot_function = plot_with_matplotlib

    plot_function(x_vals, y_vals, labels, fileLabel)


def reduce_dimensions(model):
    """https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html"""
    num_dimensions = 2  # final num dimensions (2D, 3D, etc)

    vectors = []  # positions in vector space
    labels = []  # keep track of words to label our data again later
    for word in model.wv.vocab:
        vectors.append(model.wv[word])
        labels.append(word)

    # convert both lists into numpy vectors for reduction
    vectors = np.asarray(vectors)
    labels = np.asarray(labels)

    # reduce using t-SNE
    vectors = np.asarray(vectors)
    tsne = TSNE(n_components=num_dimensions, random_state=0)
    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    return x_vals, y_vals, labels


def plot_with_plotly(x_vals, y_vals, labels, plot_in_notebook=True):
    """https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html"""
    from plotly.offline import init_notebook_mode, iplot, plot
    import plotly.graph_objs as go

    trace = go.Scatter(x=x_vals, y=y_vals, mode="text", text=labels)
    data = [trace]

    if plot_in_notebook:
        init_notebook_mode(connected=True)
        iplot(data, filename="word-embedding-plot")
    else:
        plot(data, filename="word-embedding-plot.html")


def plot_with_matplotlib(x_vals, y_vals, labels, fileLabel):
    """https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html"""
    import matplotlib.pyplot as plt
    import random

    random.seed(0)

    plt.figure(figsize=(12, 12))
    plt.scatter(x_vals, y_vals)

    #
    # Label randomly subsampled 25 data points
    #
    indices = list(range(len(labels)))
    selected_indices = random.sample(indices, 25)
    for i in selected_indices:
        plt.annotate(labels[i], (x_vals[i], y_vals[i]))
    fileLabel = fileLabel + ".pdf"
    plt.savefig(fileLabel)
