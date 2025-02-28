from hw6_language import *

### WEEK 1 TESTS ###

def testLoadBook():
    print("Testing loadBook()...", end="")
    # We'll test with two shorts files, test1.txt and test2.txt
    # Open them up to see the contents!
    assert(loadBook("data/test1.txt") == [ 
        ["hello", "and", "welcome", "to", "15-110", "."],
        ["we're", "happy", "to", "have", "you", "."] ])
    assert(loadBook("data/test2.txt") == [ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ])
    print("... done!")

def testGetCorpusLength():
    print("Testing getCorpusLength()...", end="")
    assert(getCorpusLength([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == 5)
    assert(getCorpusLength([ 
        ["hello", "and", "welcome", "to", "15-110", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == 12)
    assert(getCorpusLength([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == 41)
    print("... done!")

def testBuildVocabulary():
    print("Testing buildVocabulary()...", end="")
    assert(sorted(buildVocabulary([ 
        ["hello", "world"],
        ["hello", "world", "again"] ])) == sorted([ "hello", "world", "again"]))
    assert(sorted(buildVocabulary([ 
        ["hello", "and", "welcome", "to", "15-110", "."],
        ["we're", "happy", "to", "have", "you", "."] ])) == \
        sorted([ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"]))
    assert(sorted(buildVocabulary([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ])) == \
        sorted([ "this", "is", "the", "song", "that", "never", "ends", "yes", 
        "it", "goes", "on", "and", "my", "friends", "!", "some", "people", 
        "started", "singing", ",", "not", "knowing", "what", "was", 
        "now", "they", "keep", "forever", "just", "because", "." ]))
    print("... done!")

def testCountUnigrams():
    print("Testing countUnigrams()...", end="")
    assert(countUnigrams([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == { "hello" : 2, "world" : 2, "again" : 1 })
    assert(countUnigrams([ 
        ["hello", "and", "welcome", "to", "15-110", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == \
        { "hello" : 1, "and" : 1, "welcome" : 1, "to" : 2, "15-110" : 1, 
          "." : 2, "we're" : 1, "happy" : 1, "have" : 1, "you" : 1 })
    assert(countUnigrams([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == \
        { "this" : 1, "is" : 1, "the" : 1, "song" : 1, "that" : 1, "never" : 1, 
          "ends" : 1, "yes" : 1, "it" : 4, "goes" : 1, "on" : 3, "and" : 2, 
          "my" : 1, "friends" : 1, "!" : 1, "some" : 1, "people" : 1, 
          "started" : 1, "singing" : 2, "," : 2, "not" : 1, "knowing" : 1, 
          "what" : 1, "was" : 1, "now" : 1, "they" : 1, "keep" : 1, 
          "forever" : 1, "just" : 1, "because" : 1, "." : 3 })
    print("... done!")

def testGetStartWords():
    print("Testing getStartWords()...", end="")
    assert(getStartWords([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == [ "hello" ])
    assert(sorted(getStartWords([ 
        ["hello", "and", "welcome", "to", "15-110", "."],
        ["we're", "happy", "to", "have", "you", "."] ])) == \
        sorted(["hello", "we're"]))
    assert(sorted(getStartWords([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ])) == \
        sorted(["this", "yes", "some", "and"]))
    print("... done!")

def testCountStartWords():
    print("Testing countStartWords()...", end="")
    assert(countStartWords([ 
        ["hello", "world"], 
        ["hello", "world", "again"] ]) == { "hello" : 2 })
    assert(countStartWords([ 
        ["hello", "and", "welcome", "to", "15-110", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == \
        { "hello" : 1, "we're" : 1 })
    assert(countStartWords([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == \
        { "this" : 1, "yes" : 1, "some" : 1, "and" : 1 })
    # Check that start words are only counted in the start position
    assert(countStartWords([
        ["she", "said", "she", "was", "hungry"],
        ["he", "said", "she", "should", "eat"] ]) == \
        { "she" : 1, "he" : 1 })
    print("... done!")

def testCountBigrams():
    print("Testing countBigrams()...", end="")
    assert(countBigrams([ 
        ["hello", "world"],
        ["hello", "world", "again"] ]) == \
        { "hello" : { "world" : 2 }, "world" : { "again" : 1 } })
    assert(countBigrams([ 
        ["hello", "and", "welcome", "to", "15-110", "."],
        ["we're", "happy", "to", "have", "you", "."] ]) == \
        { "hello" : { "and" : 1 }, "and" : { "welcome" : 1 }, "welcome" : { "to" : 1 }, 
        "to" : { "15-110" : 1, "have" : 1 }, "15-110" : { "." : 1 }, "we're" : { "happy" : 1 }, 
        "happy" : { "to" : 1 }, "have" : { "you" : 1 }, "you" : { "." : 1 } })
    assert(countBigrams([ 
        ["this", "is", "the", "song", "that", "never", "ends"],
        ["yes", "it", "goes", "on", "and", "on", "my", "friends", "!"],
        ["some", "people", "started", "singing", "it", ",", "not", "knowing", "what", "it", "was", ","],
        ["and", "now", "they", "keep", "on", "singing", "it", "forever", "just", "because", ".", ".", "."] ]) == \
        { "this" : { "is" : 1 }, "is" : { "the" : 1 }, "the" : { "song" : 1 }, 
          "song" : { "that" : 1 }, "that" : { "never" : 1 }, "never" : { "ends" : 1 }, 
          "yes" : { "it" : 1 }, "it" : { "goes" : 1, "," : 1, "was" : 1, "forever" : 1 }, "goes" : { "on" : 1 }, 
          "on" : { "and" : 1, "my" : 1, "singing" : 1 }, "and" : { "on" : 1, "now" : 1 }, "my" : { "friends" : 1}, 
         "friends" : { "!" : 1 }, "some" : { "people" : 1 }, "people" : { "started" : 1 }, 
         "started" : { "singing" : 1 }, "singing" : { "it" : 2 }, "," : { "not" : 1 }, 
         "not" : { "knowing" : 1 }, "knowing" : { "what" : 1 }, "what" : { "it" : 1 }, 
         "was" : { "," : 1 }, "now" : { "they" : 1 }, "they" : { "keep" : 1 }, 
         "keep" : { "on" : 1 }, "forever" : { "just" : 1 }, "just" : { "because" : 1 }, 
         "because" : { "." : 1 }, "." : { "." : 2 } })
    print("... done!")

def week1Tests():
    testLoadBook()
    testGetCorpusLength()
    testBuildVocabulary()
    testCountUnigrams()
    testGetStartWords()
    testCountStartWords()
    testCountBigrams()

def runWeek1():
    book = loadBook("data/fairytales_clean.txt")
    length = getCorpusLength(book)
    uniqueWords = buildVocabulary(book)
    unigrams = countUnigrams(book)
    startWords = countStartWords(book)
    bigrams = countBigrams(book)
    print("Try adding some print statements in runWeek1() to explore the values in the varaibles above.")


### WEEK 2 TESTS ###

def testBuildUniformProbs():
    print("Testing buildUniformProbs()...", end="")
    assert(buildUniformProbs([ "hello", "world", "again"]) == [1/3, 1/3, 1/3])
    assert(buildUniformProbs(\
        [ "hello", "and", "welcome", "to", "15-110", ".","we're", "happy", "have", "you"]) == \
        [ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ])
    assert(buildUniformProbs(\
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", "on", 
          "and", "my", "friends", "!", "some", "people", "started", "singing", ",", "not", 
          "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ]) == \
        [ 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 
          1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31, 1/31 ])
    print("... done!")

def testBuildUnigramProbs():
    print("Testing buildUnigramProbs()...", end="")
    assert(buildUnigramProbs(\
        [ "hello", "world", "again"],
        { "hello" : 2, "world" : 2, "again" : 1 }, 5 ) == \
        [ 2/5, 2/5, 1/5 ])
    assert(buildUnigramProbs(\
        [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"],
        { "hello" : 1, "and" : 1, "welcome" : 1, "to" : 2, "15-110" : 1, "." : 2, 
          "we're" : 1, "happy" : 1, "have" : 1, "you" : 1 }, 12) == \
        [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ])
    assert(buildUnigramProbs(\
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", 
          "goes", "on", "and", "my", "friends", "!", "some", "people", "started", 
          "singing", ",", "not", "knowing", "what", "was", "now", "they", "keep", 
          "forever", "just", "because", "." ],
        { "this" : 1, "is" : 1, "the" : 1, "song" : 1, "that" : 1, "never" : 1, 
          "ends" : 1, "yes" : 1, "it" : 4, "goes" : 1, "on" : 3, "and" : 2, 
          "my" : 1, "friends" : 1, "!" : 1, "some" : 1, "people" : 1, 
          "started" : 1, "singing" : 2, "," : 2, "not" : 1, "knowing" : 1, 
          "what" : 1, "was" : 1, "now" : 1, "they" : 1, "keep" : 1, 
          "forever" : 1, "just" : 1, "because" : 1, "." : 3 }, 41) == \
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41 ])
    print("... done!")

def testBuildBigramProbs():
    print("Testing buildBigramProbs()...", end="")
    # since 'world' appears twice, once at the end of a sentence
    assert(buildBigramProbs(\
        { "hello" : 2, "world" : 2, "again" : 1 },
        { "hello" : { "world" : 2 }, "world" : { "again" : 1 } }) == \
        { "hello" : { "words" : ["world"], "probs" : [1] }, 
          "world" : { "words" : ["again"], "probs" : [0.5] } })
    assert(buildBigramProbs(\
        { "hello" : 1, "and" : 1, "welcome" : 1, "to" : 2, "15-110" : 1, "." : 2, "we're" : 1, "happy" : 1, "have" : 1, "you" : 1 }, 
        { "hello" : { "and" : 1 }, "and" : { "welcome" : 1 }, "welcome" : { "to" : 1 }, 
          "to" : { "15-110" : 1, "have" : 1 }, "15-110" : { "." : 1 }, "we're" : { "happy" : 1 }, 
          "happy" : { "to" : 1 }, "have" : { "you" : 1 }, "you" : { "." : 1 } }) == \
        { "hello" : { "words" : ["and"], "probs" : [1] },
          "and" : { "words" : ["welcome"], "probs" : [1] },
          "welcome" : { "words" : ["to"], "probs" : [1] },
          "to" : { "words" : ["15-110", "have"], "probs" : [0.5, 0.5] },
          "15-110" : { "words" : ["."], "probs" : [1] },
          "we're" : { "words" : ["happy"], "probs" : [1] },
          "happy" : { "words" : ["to"], "probs" : [1] },
          "have" : { "words" : ["you"], "probs" : [1] },
          "you" : { "words" : ["."], "probs" : [1] } })
    assert(buildBigramProbs(\
        { "this" : 1, "is" : 1, "the" : 1, "song" : 1, "that" : 1, "never" : 1, 
          "ends" : 1, "yes" : 1, "it" : 4, "goes" : 1, "on" : 3, "and" : 2, "my" : 1, 
          "friends" : 1, "!" : 1, "some" : 1, "people" : 1, "started" : 1, "singing" : 2, 
          "," : 2, "not" : 1, "knowing" : 1, "what" : 1, "was" : 1, "now" : 1, "they" : 1, 
          "keep" : 1, "forever" : 1, "just" : 1, "because" : 1, "." : 3 }, 
        { "this" : { "is" : 1 }, "is" : { "the" : 1 }, "the" : { "song" : 1 }, 
          "song" : { "that" : 1 }, "that" : { "never" : 1 }, "never" : { "ends" : 1 }, 
          "yes" : { "it" : 1 }, "it" : { "goes" : 1, "," : 1, "was" : 1, "forever" : 1 }, 
          "goes" : { "on" : 1 }, "on" : { "and" : 1, "my" : 1, "singing" : 1 }, 
          "and" : { "on" : 1, "now" : 1 }, "my" : { "friends" : 1}, "friends" : { "!" : 1 }, 
          "some" : { "people" : 1 }, "people" : { "started" : 1 }, "started" : { "singing" : 1 }, 
          "singing" : { "it" : 2 }, "," : { "not" : 1 }, "not" : { "knowing" : 1 },
          "knowing" : { "what" : 1 }, "what" : { "it" : 1 }, "was" : { "," : 1 },
          "now" : { "they" : 1 }, "they" : { "keep" : 1 }, "keep" : { "on" : 1 },
          "forever" : { "just" : 1 }, "just" : { "because" : 1 }, 
          "because" : { "." : 1 }, "." : { "." : 2 } }) == \
        { "this" : { "words" : ["is"], "probs" : [1] },
          "is" : { "words" : ["the"], "probs" : [1] },
          "the" : { "words" : ["song"], "probs" : [1] },
          "song" : { "words" : ["that"], "probs" : [1] },
          "that" : { "words" : ["never"], "probs" : [1] },
          "never" : { "words" : ["ends"], "probs" : [1] },
          "yes" : { "words" : ["it"], "probs" : [1] },
          "it" : { "words" : ["goes", ",", "was", "forever"], "probs" : [0.25, 0.25, 0.25, 0.25] },
          "goes" : { "words" : ["on"], "probs" : [1] },
          "on" : { "words" : ["and", "my", "singing"], "probs" : [1/3, 1/3, 1/3] },
          "and" : { "words" : ["on", "now"], "probs" : [0.5, 0.5] },
          "my" : { "words" : ["friends"], "probs" : [1] },
          "friends" : { "words" : ["!"], "probs" : [1] },
          "some" : { "words" : ["people"], "probs" : [1] },
          "people" : { "words" : ["started"], "probs" : [1] },
          "started" : { "words" : ["singing"], "probs" : [1] },
          "singing" : { "words" : ["it"], "probs" : [1] },
          "," : { "words" : ["not"], "probs" : [0.5] }, # because the total count of "," is 2, with one at the end
          "not" : { "words" : ["knowing"], "probs" : [1] },
          "knowing" : { "words" : ["what"], "probs" : [1] },
          "what" : { "words" : ["it"], "probs" : [1] },
          "was" : { "words" : [","], "probs" : [1] },
          "now" : { "words" : ["they"], "probs" : [1] },
          "they" : { "words" : ["keep"], "probs" : [1] },
          "keep" : { "words" : ["on"], "probs" : [1] },
          "forever" : { "words" : ["just"], "probs" : [1] },
          "just" : { "words" : ["because"], "probs" : [1] },
          "because" : { "words" : ["."], "probs" : [1] },
          "." : { "words" : ["."], "probs" : [2/3] } }) # because the total count is 3

    # One final test to make sure probabilities aren't always the same
    assert(buildBigramProbs(\
        { "one" : 3 }, 
        { "one" : { "a" : 1, "b" : 2 } }) == \
        { "one" : { "words" : ["a", "b"], "probs" : [1/3, 2/3] } })
    print("... done!")

def testGetTopWords():
    import math
    print("Testing getTopWords()...", end="")
    assert(getTopWords(2, [ "hello", "world", "again"], [2/5, 2/5, 1/5], []) == \
        { "hello" : 2/5, "world" : 2/5 })
    assert(getTopWords(3, [ "hello", "world", "again"], [2/5, 2/5, 1/5], []) == \
        { "hello" : 2/5, "world" : 2/5, "again" : 1/5 })
    assert(getTopWords(2, 
        [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"], 
        [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ], []) == \
        { "to" : 2/12, "." : 2/12 })
    assert(getTopWords(3, 
        [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"], 
        [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ], 
        [ ".", "hello", "and", "15-110", "we're", "have", "you"]) == \
        { "to" : 2/12, "welcome" : 1/12, "happy" : 1/12 })
    assert(getTopWords(1, 
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", 
          "on", "and", "my", "friends", "!", "some", "people", "started", "singing", 
          ",", "not", "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ], 
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41, 
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41], []) == \
        { "it" : 4/41 })
    assert(getTopWords(3, 
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", 
          "on", "and", "my", "friends", "!", "some", "people", "started", "singing", 
          ",", "not", "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ], 
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41], []) == \
        { "it" : 4/41, "on" : 3/41, "." : 3/41 })
    assert(getTopWords(6, 
        [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", "goes", 
          "on", "and", "my", "friends", "!", "some", "people", "started", "singing", 
          ",", "not", "knowing", "what", "was", "now", "they", "keep", "forever", "just", "because", "." ], 
        [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 2/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 2/41, 2/41, 1/41, 1/41, 1/41, 1/41,
          1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41], []) == \
        { "it" : 4/41, "on" : 3/41, "." : 3/41, "and" : 2/41, "singing" : 2/41, "," : 2/41 })
    
    words = ['though', ',', 'in', 'reviewing', 'the', 'incidents', 'of', 'my', 'administration', 'I', 'am', 'unconscious', 'intentional', 'error', 'nevertheless', 'too', 'sensible', 'defects', 'not', 'to', 'think', 'it', 'probable', 'that', 'may', 'have', 'committed', 'many', 'errors', '.', 'shall', 'also', 'carry', 'with', 'me', 'hope', 'country', 'will', 'view', 'them', 'indulgence', ';', 'and', 'after', 'forty', '-', 'five', 'years', 'life', 'dedicated', 'its', 'service', 'an', 'upright', 'zeal', 'faults', 'incompetent', 'abilities', 'be', 'consigned', 'oblivion', 'as', 'myself', 'must', 'soon', 'mansions', 'rest', 'anticipate', 'pleasing', 'expectation', 'retreat', 'which', 'promise', 'realize', 'sweet', 'enjoyment', 'partaking', 'midst', 'fellow', 'citizens', 'benign', 'influence', 'good', 'laws', 'under', 'a', 'free', 'government', 'ever', 'favorite', 'object', 'heart', 'happy', 'reward', 'trust', 'our', 'mutual', 'cares', 'labors', 'danger']
    probs = [0.006134969325153374, 0.06748466257668712, 0.018404907975460124, 0.006134969325153374, 0.05521472392638037, 0.006134969325153374, 0.06748466257668712, 0.03680981595092025, 0.006134969325153374, 0.049079754601226995, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.03067484662576687, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.024539877300613498, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.018404907975460124, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.024539877300613498, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.018404907975460124, 0.006134969325153374, 0.006134969325153374, 0.018404907975460124, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.012269938650306749, 0.012269938650306749, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374, 0.006134969325153374]
    result1 = getTopWords(8, words + [], probs + [], [])
    keys1 = sorted(list(result1.keys()))
    assert(keys1 == [',', 'I', 'my', 'of', 'that', 'the', 'to', 'with'])
    assert(math.isclose(result1[','], 0.06748466257668712, rel_tol=0.0001))
    assert(math.isclose(result1['of'], 0.06748466257668712, rel_tol=0.0001))
    assert(math.isclose(result1['the'], 0.05521472392638037, rel_tol=0.0001))
    assert(math.isclose(result1['I'], 0.049079754601226995, rel_tol=0.0001))
    assert(math.isclose(result1['my'], 0.03680981595092025, rel_tol=0.0001))
    assert(math.isclose(result1['to'], 0.03067484662576687, rel_tol=0.0001))
    assert(math.isclose(result1['that'], 0.024539877300613498, rel_tol=0.0001))
    assert(math.isclose(result1['with'], 0.024539877300613498, rel_tol=0.0001))

    result2 = getTopWords(5, words + [], probs + [], [',', '.', '-', ';'])
    keys2 = sorted(list(result2.keys()))
    assert(keys2 == ['I', 'my', 'of', 'the', 'to'])
    assert(math.isclose(result2['of'], 0.06748466257668712, rel_tol=0.0001))
    assert(math.isclose(result2['the'], 0.05521472392638037, rel_tol=0.0001))
    assert(math.isclose(result2['I'], 0.049079754601226995, rel_tol=0.0001))
    assert(math.isclose(result2['my'], 0.03680981595092025, rel_tol=0.0001))
    assert(math.isclose(result2['to'], 0.03067484662576687, rel_tol=0.0001))    

    # testing for not destructively changing ignore list, worse, or probs
    ignore = [ ".", "hello", "and", "15-110", "we're", "have", "you"]
    words = [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"]
    probs = [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ]
    result = getTopWords(3, 
        [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"], 
        [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ],
        ignore)
    assert(ignore == [ ".", "hello", "and", "15-110", "we're", "have", "you"])
    assert(words == [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you"])
    assert(probs == [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ])
    print("... done!")

def testGenerateTextFromUnigrams():
    print("Testing generateTextFromUnigrams()...", end="")
    # Since this is random, we can only check that it's the right length
    # and that it only uses words in the provided list.
    words = [ "hello", "world", "again" ]
    probs = [ 2/5, 2/5, 1/5 ]
    sentence = generateTextFromUnigrams(5, words, probs)
    assert(len(sentence.strip().split(" ")) == 5)
    for word in sentence.strip().split(" "):
        assert(word in words)

    words = [ "hello", "and", "welcome", "to", "15-110", ".", "we're", "happy", "have", "you" ]
    probs = [ 1/12, 1/12, 1/12, 2/12, 1/12, 2/12, 1/12, 1/12, 1/12, 1/12 ]
    sentence = generateTextFromUnigrams(10, words, probs)
    assert(len(sentence.strip().split(" ")) == 10)
    for word in sentence.strip().split(" "):
        assert(word in words)

    words = [ "this", "is", "the", "song", "that", "never", "ends", "yes", "it", 
              "goes", "on", "and", "my", "friends", "!", "some", "people", "started", 
              "singing", ",", "not", "knowing", "what", "was", "now", "they", "keep", 
              "forever", "just", "because", "." ]
    probs = [ 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 4/41, 1/41, 3/41, 
              2/41, 1/41, 1/41, 1/41, 1/41, 1/41,  1/41, 2/41, 2/41, 1/41, 1/41, 
              1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 1/41, 3/41 ]
    sentence = generateTextFromUnigrams(20, words, probs)
    assert(len(sentence.strip().split(" ")) == 20)
    for word in sentence.strip().split(" "):
        assert(word in words)
    print("... done!")

def testGenerateTextFromBigrams():
    print("Testing generateTextFromBigrams()...", end="")
    # Since we assume . is used as a stopping point, include it specifically in the test set.
    startWords = [ "hi", "dear" ]
    startProbs = [ 0.6, 0.4 ]
    bigramProbs = { 
        "hi" : { "words" : [",", "how"], "probs" : [0.8, 0.2] },
        "dear" : { "words" : [ "sir", "madam" ], "probs" : [0.5, 0.5] },
        "," : { "words" : ["what's", "sup", "yeet"], "probs" : [0.3, 0.3, 0.4] },
        "how" : { "words" : ["are"], "probs" : [1] },
        "sir" : { "words" : [".", ","], "probs" : [0.8, 0.2] },
        "madam" : { "words" : [ ".", ","], "probs" : [0.8, 0.2] },
        "what's" : { "words" : [ "up" ], "probs" : [1] },
        "sup" : { "words" : [ "." ], "probs" : [1] },
        "yeet" : { "words" : [ "!" ], "probs" : [1] },
        "are" : { "words" : [ "you", "yeet" ], "probs" : [0.9, 0.1] },
        "up" : { "words" : [ ".", "," ], "probs" : [0.5, 0.5] },
        "!" : { "words" : ["!", "."], "probs" : [0.7, 0.3] },
        "you" : { "words" : ["."], "probs" : [1] } }

    sentence = generateTextFromBigrams(10, startWords, startProbs, bigramProbs)
    sentenceWords = sentence.strip().split()
    assert(len(sentenceWords) == 10)

    # Check that the order of words is legal
    for i in range(len(sentenceWords)):
        if i == 0 or sentenceWords[i-1] == ".":
            assert(sentenceWords[i] in startWords)
        else:
            assert(sentenceWords[i] in bigramProbs[sentenceWords[i-1]]["words"])
    print("... done!")

def week2Tests():
    testBuildUniformProbs()
    testBuildUnigramProbs()
    testBuildBigramProbs()
    testGetTopWords()
    testGenerateTextFromUnigrams()
    testGenerateTextFromBigrams()

def runWeek2():
    # Check-in 1 Functions
    book = loadBook("data/fairytales_clean.txt")
    length = getCorpusLength(book)
    uniqueWords = buildVocabulary(book)
    startWords = getStartWords(book)
    unigramCounts = countUnigrams(book)
    startWordCounts = countStartWords(book)
    bigramCounts = countBigrams(book)

    # Uniform Model
    uniformProbs = buildUniformProbs(uniqueWords)
    print("\nText generated by the Uniform Model:\n")
    print(generateTextFromUnigrams(100, uniqueWords, uniformProbs))
    print("\n-----\n")

    # Unigram Model
    unigramProbs = buildUnigramProbs(uniqueWords, unigramCounts, length)
    startWordProbs = buildUnigramProbs(startWords, startWordCounts, len(book))
    print("Top 20 words in the Unigram Model:")
    print(getTopWords(20, uniqueWords, unigramProbs, []))
    print("\nTop 20 starting words in the Unigram Model:")
    print(getTopWords(20, startWords, startWordProbs, []))
    print("\nText generated by the Unigram Model:\n")
    print(generateTextFromUnigrams(100, uniqueWords, unigramProbs))
    print("\n-----\n")

    # Bigram Model
    bigramProbs = buildBigramProbs(unigramCounts, bigramCounts)
    print("Text generated by the Bigram Model:\n")
    print(generateTextFromBigrams(100, startWords, startWordProbs, bigramProbs))


### WEEK 3 TESTS ###

def testSetupChartData():
    import math
    print("Testing setupChartData()...", end="")
    book1 = loadBook("data/grimm_clean.txt")
    book2 = loadBook("data/andersen_clean.txt")
    result = setupChartData(book1, book2, 50)
    assert(len(result) == 3) # should be a dictionary with three keys
    assert("topWords" in result)
    assert("corpus1Probs" in result)
    assert("corpus2Probs" in result)
    assert(len(result["topWords"]) == 62) # 62 unique top-words should be found
    assert(result["topWords"][0] == "he")
    assert(result["topWords"][5] == "i")
    assert(len(result["corpus1Probs"]) == 62) # one probability per word
    # For float comparison, just check if they're close enough
    assert(math.isclose(result["corpus1Probs"][0], 0.01756494170587032, rel_tol=0.0001))
    assert(math.isclose(result["corpus1Probs"][5], 0.008880479989091156, rel_tol=0.0001))
    assert(len(result["corpus2Probs"]) == 62)
    assert(math.isclose(result["corpus2Probs"][0], 0.012816268621423505, rel_tol=0.0001))
    assert(math.isclose(result["corpus2Probs"][5], 0.010262473397966423, rel_tol=0.0001))
    
    result2 = setupChartData(book1, book2, 30)
    assert(len(result2["topWords"]) == 35) # should only count topWordCount words - for 30, the overlap leads to 35 unique unigrams
    print("... done!")

def runWeek3():
    book1 = loadBook("data/grimm_clean.txt")
    book2 = loadBook("data/andersen_clean.txt")
    
    graphTop50Words(book1)
    graphTopStartWords(book1)
    graphTopNextWords(book1, "said")
    graphTopNextWords(book2, "said")
    graphTopNextWords(book1, "good")
    graphTopNextWords(book2, "good")

    testSetupChartData()
    
    graphTopWordsSideBySide(book1, "Grimm", book2, "Andersen", 50, "Top 50 Words in Grimm vs Andersen")
    graphTopWordsInScatterplot(book1, book2, 30, "Top 30 Words in Grimm vs Andersen")