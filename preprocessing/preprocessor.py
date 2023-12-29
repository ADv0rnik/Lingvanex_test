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


class UnicodeCleaner(PreprocessorABC):
    """
    The class helps to remove unprintable characters and left only ASCII printable characters.
    No input arguments required
    """

    @staticmethod
    def __remove_unprintable(segment):
        printable_segment = ''.join(x for x in segment if x.isprintable())
        return printable_segment

    def process(self, pairs):
        for segments in pairs:
            yield [self.__remove_unprintable(segment) for segment in segments]
