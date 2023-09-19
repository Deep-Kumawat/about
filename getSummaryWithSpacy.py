# Remove stop words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

inputText = """"""

def createFrequencyTable(inputText):
    """creates a frequency table for all the words after removing stop words and reducing them to their root form"""
    #remove stop words
    stopWords = set(stopwords.words("english"))

    #tokenizing words
    words = word_tokenize(inputText)

    #Reducing the words to it's root form using PorterStemmer
    stem = PorterStemmer()

    #Creating dictionary for the word frequency table
    frequencyTable = dict()
    for w in words:
        wd = stem.stem(w) #Reduces the current word to it's root form
        if w in stopWords:
            continue
        if w in frequencyTable:
            frequencyTable[w] += 1
        else:
            frequencyTable[w] = 1

    return frequencyTable

sentences = sent_tokenize(inputText)

def calculateSentenceScores(sentences, frequency_table) -> dict:   
    """Returns a dictionary with a sentence's first 7 characters as key and its score as its value
        The score is calculated by dividing the sum of frequencies of all the words in that sentence by number of words"""
    sentenceScoreDict = dict()
    for sentence in sentences:
        wordCount = 0
        # sentenceScoreDict[sentence[:7]] = 0
        sentenceScoreDict[sentence] = 0
        for word in frequency_table:
            if word in sentence.lower():
                # sentenceScoreDict[sentence[:7]] += frequency_table[word]
                sentenceScoreDict[sentence] += frequency_table[word]
                wordCount+=1
        # sentenceScoreDict[sentence[:7]] /= wordCount
        sentenceScoreDict[sentence] /= wordCount

    return sentenceScoreDict

def getTopRatedSentence(senctenceScoresDictionary):
    max = 0
    key = ""
    for value in senctenceScoresDictionary:
        if senctenceScoresDictionary[value] > max:
            max = senctenceScoresDictionary[value]
            key = value
    return key

def getAverageSentenceScore(senctenceScoresDictionary):
    score = 0
    for key in senctenceScoresDictionary:
        score += senctenceScoresDictionary[key]
    score /= len(senctenceScoresDictionary)
    return score

def getSummary(sentences, sentenceScoreDictionary, averageScore):
    # sentenceCounter = 0
    summary = ''

    for sentence in sentences:
        if sentence in sentenceScoreDictionary and sentenceScoreDictionary[sentence] >= averageScore:
            summary += " " + sentence
            # sentenceCounter += 1

    return summary

#calling functions
dict1 = calculateSentenceScores(sentences, createFrequencyTable(inputText))
# print(createFrequencyTable(inputText))
# print(sentences)
# print()
# print(calculateSentenceScores(sentences, createFrequencyTable(inputText)))

# print("the top rated sentence is:\n")
# print(getTopRatedSentence(calculateSentenceScores(sentences, createFrequencyTable(inputText))))

# print(getAverageSentenceScore(dict1))
# print(getSummary(sentences, dict1, 2.1))
print(getTopRatedSentence(dict1))