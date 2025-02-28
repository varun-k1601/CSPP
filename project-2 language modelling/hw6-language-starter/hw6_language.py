"""
15-110 Hw6 - Language Modeling Project
Name:
AndrewID:
"""

import hw6_language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    corpus = []
    with open(filename, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                words = stripped_line.split()
                corpus.append(words)
    return corpus



'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    corpus_len=0
    for i in corpus:
        corpus_len+=len(i)
    return corpus_len


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    vocabulary=[]
    for sentence in corpus:
        for word in sentence:
            if word not in vocabulary:
                vocabulary.append(word)
    return vocabulary


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    unigram_count={}
    for sentence in corpus:
        for word in sentence:
            if word not in unigram_count:
                unigram_count[word]=1
            else:
                unigram_count[word]+=1
    return unigram_count


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    start_words=[]
    for i in corpus:
        if i[0] not in start_words:
            start_words.append(i[0])
    return start_words


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    start_words_count = {}
    for i in corpus:
        if start_words_count.get(i[0]) == None:
            start_words_count[i[0]] = 1
        else:
            start_words_count[i[0]] += 1
    return start_words_count


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    bigram_dict = {}
    for l in corpus:
        for i in range(len(l) - 1):
            bigram = [l[i], l[i+1]]
            if bigram_dict.get(bigram[0]) == None:
                bigram_dict[bigram[0]] = {bigram[1]: 1}
            elif bigram_dict[bigram[0]].get(bigram[1]) == None:
                bigram_dict[bigram[0]][bigram[1]] = 1
            else:
                bigram_dict[bigram[0]][bigram[1]] += 1
    return bigram_dict


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    probabilities = []
    probability_value = 1 / len(unigrams)
    for _ in range(len(unigrams)):
        probabilities.append(probability_value)
    return probabilities


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    probabilities = []
    for i in range(len(unigrams)):
        probability = unigramCounts[unigrams[i]] / totalCount
        probabilities.append(probability)
    return probabilities


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    bigram_probs = {}
    
    for first_word in bigramCounts:
        bigram_probs[first_word] = {"words": [], "probs": []}
        
        for second_word in bigramCounts[first_word]:
            bigram_probs[first_word]["words"].append(second_word)
            probability = bigramCounts[first_word][second_word] / unigramCounts[first_word]
            bigram_probs[first_word]["probs"].append(probability)
    
    return bigram_probs


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    top_words = {}
    indexed_probs = list(zip(words, probs))  # Combine words and probabilities

    # Sort by probability in descending order
    indexed_probs.sort(key=lambda x: x[1], reverse=True)

    for word, prob in indexed_probs:
        if word not in ignoreList and len(top_words) < count:
            top_words[word] = prob
            
    return top_words

'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    words_list = []
    for i in range(count):
        words_list.extend(choices(words, weights=probs))
    return " ".join(words_list)


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    words_list = []
    for _ in range(count):
        if len(words_list) == 0 or words_list[-1] == '.':
            words_list.extend(choices(startWords, weights= startWordProbs))
        else:
            words_list.extend(choices(bigramProbs[words_list[-1]]["words"], weights= bigramProbs[words_list[-1]]["probs"]))
    return " ".join(words_list)


### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    unigram_count = countUnigrams(corpus)
    unigram_probs = buildUnigramProbs(list(unigram_count.keys()), unigram_count, len(unigram_count))
    top_words = getTopWords(50, list(unigram_count.keys()), unigram_probs, ignore)
    
    barPlot(top_words, title="Top 50 Words")


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    start_words = getStartWords(corpus)
    start_words_count = countStartWords(corpus)
    start_words_probs = buildUnigramProbs(start_words, start_words_count, len(start_words))
    top_start_words = getTopWords(50, start_words, start_words_probs, ignore)

    barPlot(top_start_words, title="Top 50 start words")


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    unigram_counts = countUnigrams(corpus)
    bigram_counts = countBigrams(corpus)
    bigrams = buildBigramProbs(unigram_counts, bigram_counts)
    top_next_words = getTopWords(10, bigrams[word]["words"], bigrams[word]["probs"], ignore)

    barPlot(top_next_words, title="Top 10 next words")


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    corpus_1_length = getCorpusLength(corpus1)
    corpus_1_unigram_count = countUnigrams(corpus1)
    corpus_1_unigram_probs = buildUnigramProbs(list(corpus_1_unigram_count.keys()), corpus_1_unigram_count, corpus_1_length)
    corpus_1_top_words = getTopWords(topWordCount, list(corpus_1_unigram_count.keys()), corpus_1_unigram_probs, ignore)

    corpus_2_length = getCorpusLength(corpus2)
    corpus_2_unigram_count = countUnigrams(corpus2)
    corpus_2_unigram_probs = buildUnigramProbs(list(corpus_2_unigram_count.keys()), corpus_2_unigram_count, corpus_2_length)
    corpus_2_top_words = getTopWords(topWordCount, list(corpus_2_unigram_count.keys()), corpus_2_unigram_probs, ignore)

    top_words_combined  = corpus_1_top_words.copy()
    for word in corpus_2_top_words:
        if word in top_words_combined:
            top_words_combined[word] += corpus_2_top_words[word]
        else:
            top_words_combined[word] = corpus_2_top_words[word]
    # print(top_words_combined)
    # print("\n".join(list(top_words_combined.keys())))
    corpus_1_probs, corpus_2_probs = {}, {}

    for word in top_words_combined:
        if word in corpus_1_top_words:
            corpus_1_probs[word] = corpus_1_top_words[word]
        else:
            corpus_1_probs[word] = 0
        
        if word in corpus_2_top_words:
            corpus_2_probs[word] = corpus_2_top_words[word]
        else:
            corpus_2_probs[word] = 0 
    output = {"topWords": list(top_words_combined.keys()), 
              "corpus1Probs": list(corpus_1_probs.values()),
              "corpus2Probs": list(corpus_2_probs.values())
            }
    return output



'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    corpora_probs = setupChartData(corpus1, corpus2, numWords)

    sideBySideBarPlots(corpora_probs["topWords"], 
                       corpora_probs["corpus1Probs"], 
                       corpora_probs["corpus2Probs"],
                       name1,
                       name2,
                       title)


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    corpora_probs = setupChartData(corpus1, corpus2, numWords)

    scatterPlot(corpora_probs["corpus1Probs"], 
                corpora_probs["corpus2Probs"], 
                corpora_probs["topWords"],
                title)


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    test.runWeek1()

    ## Uncomment these for Week 2 ##

    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    test.runWeek2()


    ## Uncomment these for Week 3 ##

    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()