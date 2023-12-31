import math
import re

from string import ascii_lowercase, ascii_uppercase
from enum import Enum

from enchant.checker import SpellChecker
from enchant.tokenize import WikiWordFilter, Filter
from opusfilter import FilterABC, CLEAN_BETWEEN, CLEAN_TRUE, logger
from exceptions.opus_exceptions import OpusUnexpectedException


class LanguageSchema(Enum):
    ENGLISH = 'en_US'
    RUSSIAN = 'ru_RU'


class EngCapitalizeWordsFilter(Filter):
    eng_pattern = re.compile(r"\b[A-Z][a-zA-Z]*\b")

    def _skip(self, word):
        return True if self.eng_pattern.match(word) else False


class RusCapitalizeWordsFilter(Filter):
    rus_pattern = re.compile(r"[А-Я][А-я]*")

    def _skip(self, word):
        return True if self.rus_pattern.match(word) else False


class GrammarFilter(FilterABC):
    """
    The filter checks whether the segment contains mistakes or wrong spelling words
    """

    score_direction = CLEAN_TRUE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def create_checker(lang: LanguageSchema) -> SpellChecker:
        _checker = SpellChecker(
            lang=lang.value,
            filters=[EngCapitalizeWordsFilter, RusCapitalizeWordsFilter]
        )
        return _checker

    @staticmethod
    def is_english(sample: str):
        alpha = ascii_uppercase + ascii_lowercase
        return any([True if char in alpha else False for char in sample])

    def __check_grammar(self, segment: str):
        if self.is_english(segment.split()[0]):
            checker = self.create_checker(LanguageSchema.ENGLISH)
        else:
            checker = self.create_checker(LanguageSchema.RUSSIAN)
        checker.set_text(segment)

        try:
            found = bool([i.word for i in checker])
        except OpusUnexpectedException as error:
            logger.error(f"{error}")
            found = True
        return found

    def score(self, pairs):
        for pair in pairs:
            yield [self.__check_grammar(sentence) for sentence in pair]

    def accept(self, score):
        return not any(score)


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
