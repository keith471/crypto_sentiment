'''Aggregates the scores of a group of text summaries'''

class Aggregator(object):

    @staticmethod
    def add(summaries):
        total = 0.0
        for summary in summaries:
            total += (summary.score * summary.provider.weight)
        return total
