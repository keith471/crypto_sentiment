'''Represents a Tweet'''

class TweetSummary(TextSummary):

    def __init__(self, provider, text, coin, sentiment, created_at, updated_at, posted_at, tags, user_id, reshare_count, reshare_users):
        self.posted_at = posted_at
        self.tags = tags
        self.user_id = user_id
        self.reshare_count = reshare_count
        self.reshare_users = reshare_users
        super(TweetSummary, self).__init__(provider, text, coin, sentiment, created_at, updated_at)

    def compute_score(self):
        '''
        The score of a tweet is computed as the sentiment times the reshare count.
        '''
        return self.sentiment * self.reshare_count
