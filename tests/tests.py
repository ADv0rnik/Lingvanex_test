import unittest
import random

from pathlib import Path
from opusfilter.opusfilter import OpusFilter


BASE_DIR = Path(__file__).resolve().parent.parent


class TestTenWordsLengthFilter(unittest.TestCase):
    
    def setUp(self) -> None:
        self.config = {
            'steps': [
                {
                    'type': 'filter',
                    'parameters': {
                        'inputs': [
                            'text.en-ru.en',
                            'text.en-ru.ru'
                        ],
                        'outputs': [
                            'text_f.en-ru.en',
                            'text_f.en-ru.ru'
                        ],
                        'cstm_filters': [{
                            'TenWordsLengthFilter': {
                                'unit': 'word',
                                'max_length': 10
                            },
                            'module': 'len_filter'
                        }]
                    }
                }
            ]
        }
        self.opus_filter = OpusFilter(self.config)
        self.opus_filter.execute_steps()

    def test_get_length(self):
        test_string = "We need more heroines like you, Tina."
        self.assertEqual(len(test_string), 37)

    def test_output_file(self):
        indx = random.randint(0, 100)
        try:
            with open("text_f.en-ru.en", "r") as file:
                data = file.readlines()
                random_segment = data[indx].split()
                self.assertLessEqual(len(random_segment), 10)    
        except FileNotFoundError as error:
            print(error)
        except IndexError as error_:
            print(error_)
