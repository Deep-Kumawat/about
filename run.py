from transcript import *
from summary import *


# userInputURL = input("Enter URL")
userInputURL = "https://www.youtube.com/watch?v=xC-c7E5PK0Y"
transcriptObject = Transcript(userInputURL)
summaryObject = Summary()

# transcriptStringVariable = transcriptObject.getTranscriptStringVariable()
averageSentenceScore = summaryObject.getAverageSentenceScore()

# To control the number of sentences in the summary, getSummary() function's argument can be changed.
# To get more lines we can decrease the score and vice versa

# lower score = lesser lines
SCORE = averageSentenceScore
print("---------------------------------------------------------------------------------------------------------------------")
print(f"THE BELOW SUMMARY COMPRISES OF ALL THE SENTENCES WHICH HAVE A SENTENCE SCORE HIGHER THAN AVERAGE (AVG: {SCORE})")
print("---------------------------------------------------------------------------------------------------------------------")
print(summaryObject.getSummary(SCORE))

# higher score = more lines
SCORE = averageSentenceScore + 2.25 # 15 is an arbitrary number
print("---------------------------------------------------------------------------------------------------------------------")
print(f"THE BELOW SUMMARY IS OF SCORE: {SCORE}")
print("---------------------------------------------------------------------------------------------------------------------")
print(summaryObject.getSummary(SCORE))
print("---------------------------------------------------------------------------------------------------------------------")