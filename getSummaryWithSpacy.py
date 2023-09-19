# Remove stop words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

inputText = """Why Is the Sky Blue?
In the middle of a bright, sunny day, the
sky is usually a shade of blue.
Why blue—and not purple, green, or orange?
Well, it’s all because of how the Sun’s
light reaches Earth!
If you see light from the Sun hitting the
ground, it probably looks like plain white
light.
However, that white light is made up of all
the colors of the rainbow.
You can actually separate and see all these
colors if you shine sunlight through a specially
shaped crystal called a prism.
Light energy travels in waves.
And different colors of light are created
by different types of waves.
For example, when our eyes recognize the color
red, what we’re actually seeing is long,
stretched-out light waves with peaks that
are far apart.
And when our eyes recognize the color blue,
we’re really seeing shorter, choppier light
waves with peaks that are close together.
The different colors of light are all determined
by how stretched out the light waves are.
Together, all the colors make up the spectrum
of visible light—the light we can see.
So, why do we only see blue light when we
look up in the sky on a sunny day?
The blue color we see comes from sunlight
hitting Earth’s atmosphere—a layer of
gases that gives us air to breathe and keeps
the planet warm enough to live on.
When sunlight reaches Earth’s atmosphere,
it is scattered in all directions by the gases
in the air.
The types of gases in Earth’s atmosphere
mostly scatter the shorter, choppier waves
of blue light.
So, when we see a blue sky, we’re really
just seeing all of these blue light waves
scattering in our atmosphere.
But wait a minute: why is the sky a different
color at sunset?
Well, as the Sun gets lower in the sky, its
light is passing through more of the atmosphere
to reach you.
So, even more of the blue light is scattered
away before it gets to you.
This allows more of the orange and yellow
light to pass straight through the atmosphere
and directly to your eyes.
However if the whole sky is glowing red, it
could be due to particles of dust, pollution,
or smoke in the air.
These particles also scatter lots of blue
light, which can lead to a very red sky.
NASA’s Earth-observing satellites monitor
how many of these particles—called aerosols—are
in our air.
The information from these satellites help
forecasters keep an eye on particles in the
air and make sure the air is safe to breathe.
In general, a blue sky is good news.
And now you know why!
Find out more about our home planet at NASA
Space Place.

"""

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

def getSummary(sentences, averageScore):
    # sentenceCounter = 0
    summary = ''
    sentenceScoreDictionary = calculateSentenceScores(sentences, createFrequencyTable(inputText))
    for sentence in sentences:
        if sentence in sentenceScoreDictionary and sentenceScoreDictionary[sentence] >= averageScore:
            summary += " " + sentence
            # sentenceCounter += 1

    return summary

avgScore = getAverageSentenceScore(calculateSentenceScores(sentences, createFrequencyTable(inputText)))
print(avgScore)
#calling functions
dict1 = calculateSentenceScores(sentences, createFrequencyTable(inputText))

# print(getSummary(sentences, getAverageSentenceScore(calculateSentenceScores(sentences, createFrequencyTable(inputText)))))
print(getSummary(sentences, avgScore+1))
