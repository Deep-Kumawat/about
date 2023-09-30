# Remove stop words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from transcript import *


class Summary:

    # Initiallizing the transcript string variable
    inputText = """"""

    #this list would contain all the sentence (tokenized)
    sentences = []
    
    #constructor
    def __init__(self):
        #Copying the transcript from transcript.txt to inputText
        with open("transcript.txt", 'r') as transcriptTextFile:
            self.inputText += transcriptTextFile.read().replace('\n', '')
        #tokenizing the sentences
        self.sentences = sent_tokenize(self.inputText)

    def createFrequencyTable(self):
        """creates a frequency table for all the words after removing stop words and reducing them to their root form"""
        #remove stop words
        stopWords = set(stopwords.words("english"))

        #tokenizing words
        words = word_tokenize(self.inputText)

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


    def calculateSentenceScores(self) -> dict:   
        """Returns a dictionary with a sentence's first 7 characters as key and its score as its value
            The score is calculated by dividing the sum of frequencies of all the words in that sentence by number of words"""
        sentenceScoreDict = dict()
        frequency_table = self.createFrequencyTable()
        for sentence in self.sentences:
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

    def getAverageSentenceScore(self):
        senctenceScoresDictionary = self.calculateSentenceScores()
        score = 0
        for key in senctenceScoresDictionary:
            score += senctenceScoresDictionary[key]
        score /= len(senctenceScoresDictionary)
        return score

    def getSummary(self, averageScore):
        # sentenceCounter = 0
        summary = ''
        sentences = self.sentences
        sentenceScoreDictionary = self.calculateSentenceScores()
        for sentence in sentences:
            if sentence in sentenceScoreDictionary and sentenceScoreDictionary[sentence] >= averageScore:
                summary += " " + sentence
                # sentenceCounter += 1

        return summary


