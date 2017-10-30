'''An in-memory represensation of a text summary'''

class TextSummary(object):

    def __init__(self, provider, text, coin, sentiment, created_at, updated_at):
        self.provider = provider
        self.text = text
        self.coin = coin
        self.sentiment = sentiment
        self.created_at = created_at
        self.updated_at = updated_at
        self.score = self.compute_score()

    def compute_score(self):
        '''
        Default implementation.
        Returns the sentiment of the text.
        Should be overridden by each subclass.
        '''
        return self.sentiment
