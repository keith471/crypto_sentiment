'''Sentiment analysis using Vader model'''
from __future__ import print_function

from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyzer(object):

    ##
    # Constructor
    # @param preprocessor - The preprocessor to use in preprocessing of the text
    ##
    def __init__(self, preprocessor):
        self.sid = SentimentIntensityAnalyzer()
        self.preprocessor = preprocessor

    ##
    # Computes the sentiment for a text by averageing the sentiments of all the
    # sentences in the text
    # @param text - The text
    # @return - The average sentiment of the sentences in the text
    ##
    def get_sentiment(self, text):
        '''returns number between -1 and 1 based on overall sentiment'''
        sentences = self.preprocessor.process(text)
        total = 0.0
        count = 0
        for sentence in sentences:
            scores = self.sid.polarity_scores(sentence)
            for k in sorted(scores):
                print('{0}: {1}, '.format(k, scores[k]), end='')
            print()
            total += scores['compound']
            count += 1
        return total / float(count)
