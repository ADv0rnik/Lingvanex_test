import unittest
from len_filter import TenWordsLengthFilter
from opusfilter.opusfilter import OpusFilter


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
                        'filters': [{
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
