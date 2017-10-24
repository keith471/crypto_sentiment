'''Sentiment analysis using Vader model'''
from __future__ import print_function

from nltk import tokenize

class Preprocessor(object):

    def __init__(self):
        pass

    ##
    # Splits text into sentences
    # @param text - The text
    # @return - An array of sentences in the text
    ##
    def get_sentences(self, text):
        return tokenize.sent_tokenize(text)

    ##
    # Handles processing of the text
    # @param text - The text
    # @return - The processed text, as an array of sentences
    ##
    def process(self, text):
        return self.get_sentences(text)
