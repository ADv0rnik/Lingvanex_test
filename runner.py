import json

from pathlib import Path
from opusfilter.opusfilter import OpusFilter


BASE_DIR = Path(__file__).resolve().parent


class Filter:
    def __init__(self):
        self.__config = self.__get_config()
        self.__opus_filter = OpusFilter(configuration=self.__config)

    @staticmethod
    def __get_config():
        try:
            with open(str(BASE_DIR) + "/config.json", "r") as file:
                config_data = json.load(file)
            return config_data
        except FileNotFoundError as error:
            return error

    def return_filter_instance(self):
        return self.__opus_filter


if __name__ == '__main__':
    raw_filter = Filter()
    opus_filter_ = raw_filter.return_filter_instance()
    opus_filter_.execute_steps()


