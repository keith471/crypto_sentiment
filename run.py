'''Example using new preprocessing technique'''
from __future__ import print_function

from argparse import ArgumentParser
import sys
import os

from sentiment_analyzer import SentimentAnalyzer
from preprocessor import Preprocessor

#===============================================================================
# Arugment parsing
#===============================================================================

parser = ArgumentParser()
parser.add_argument('text', type=str, action='store',
                    help='the path of the csv to load')
parser.add_argument('--h', action='store_true',
                    help='if set, usage will be printed out')

args = parser.parse_args()

## TODO error checking on the args

if args.h:
    parser.print_help()

print()

#===============================================================================
# Main
#===============================================================================

if __name__ == '__main__':

    preproc = Preprocessor()
    analyzer = SentimentAnalyzer(preproc)

    text = args.text

    sentiment = analyzer.get_sentiment(text)

    print('Sentiment: %f' % sentiment)
    print()
