import unittest
import random

from pathlib import Path
from opusfilter.opusfilter import OpusFilter

BASE_DIR = Path(__file__).resolve().parent.parent


class TestCustomFilters(unittest.TestCase):

    def setUp(self) -> None:
        self.config = {
            'common': {
                'output_directory': 'outputs/'
            },
            'steps': [
                {
                    'type': 'filter',
                    'parameters': {
                        'inputs': [
                            'text.en-ru.en',
                            'text.en-ru.ru'
                        ],
                        'outputs': [
                            'text_test.en-ru.en',
                            'text_test.en-ru.ru'
                        ],
                        'filters': [
                            {
                                'TenWordsLengthFilter': {
                                    'unit': 'word',
                                    'max_length': 10
                                },
                                'module': 'filters'
                            },
                            {
                                'GrammarFilter': {},
                                'module': 'filters'
                            }
                        ]
                    }
                }
            ]
        }
        self.opus_filter = OpusFilter(self.config)
        self.opus_filter.execute_steps()

    def test_get_length(self):
        try:
            with open('outputs/text_test.en-ru.en', 'r') as file:
                test_string = file.readlines()[0]
                self.assertLessEqual(len(test_string), 50)
        except FileNotFoundError as error:
            print(error)

    def test_lines_filtered(self):
        tgt_num_lines = 15
        try:
            with open('outputs/text_test.en-ru.en', 'r') as file:
                source_num_lines = len(file.readlines())
                self.assertEqual(source_num_lines, tgt_num_lines)
        except FileNotFoundError as error:
            print(error)
