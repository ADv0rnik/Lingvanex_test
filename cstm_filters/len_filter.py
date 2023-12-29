import math
from opusfilter import FilterABC, CLEAN_BETWEEN


class TenWordsLengthFilter(FilterABC):
    score_direction = CLEAN_BETWEEN
    accept_threshold = (0, math.inf)
    reject_threshold = (math.inf, 0) 
           
    def __init__(self, max_length=10, pass_empty=False, **kwargs):
        if max_length != 10:
            self.max_length = 10
        else:
            self.max_length = max_length
        self.unit = 'word'
        self.pass_empty = pass_empty
        super().__init__(**kwargs)

    @staticmethod
    def get_length(segment):
        return len(segment.split())

    def score(self, pairs):
        for pair in pairs:
            yield [self.get_length(segment) for segment in pair]

    def accept(self, score):
        if self.pass_empty and sum(score) == 0:
            return True
        return all(length <= self.max_length for length in score)