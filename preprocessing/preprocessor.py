import re
from opusfilter import PreprocessorABC


class StringCleaner(PreprocessorABC):

    @staticmethod
    def __clean_string(segment):
        pattern = r'(\"\s*\.\s*)|(\")'
        segment = re.sub(pattern=pattern, repl='', string=segment, count=0)
        segment = segment.strip()
        segment = segment.strip(".")
        return segment

    def process(self, pairs):
        for segments in pairs:
            yield [self.__clean_string(segment) for segment in segments]

