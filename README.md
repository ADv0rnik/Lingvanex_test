### Text filtering

#### Background 
The current functionality of the application is based on OpusFilter toolkit: https://github.com/Helsinki-NLP/OpusFilter 
it is possible to use an overal OpusFilter functionality together with selfwritten filter classes. 
TenWordsLengthFilter - specific filter to delete all sentences longer than 10 words from provided text. The filter was tested on Ubuntu 22.04 OS

#### Usage
Before using this filter make sure that opusfilter is preinstalled on your local machine. Than follow these steps:
1. Clone the repository onto your local machine by following command:
`git clone https://github.com/ADv0rnik/Lingvanex_test.git`
or if you are using ssh
`git clone git@github.com:ADv0rnik/Lingvanex_test.git`
2. Create virtual environment by using:
`python -m venv venv`
3. Setup your `config.yml` file.
4. Add the directory that contains filter module to PYTHONPATH environment variable by using the following command:
```commandline
export PYTHONPATH="${PYTHONPATH}:/path/to/your/module/"
```
5. Navigate to `filter_handler` directory and run a single command to clean up the sample text (assuming that input files exist):
```commandline
opusfilter-cmd filter --inputs WikiMatrix.en-ru.en WikiMatrix.en-ru.ru --outputs text_f.en-ru.en text_f.en-ru.ru --filters '[{"TenWordsLengthFilter": {"max_length": 10}, "module": "len_filter"}]'
```

#### Tests
To run some tests after text cleaning use
```python
python3 -m unittest tests
```

#### Troubleshooting
Some possible issues:

**1. Module not found**

*Solution*: Make sure that you added filter module to PYTHONPATH environment variable. Check it with Python `sys` module

```python
import sys
print(sys.path)
```

**2. opusfilter.ConfigurationError: Number of input and output files should match in sort**

The filter command requires a list of input files as well as the similar number of output files

*Solution*: Make sure that the number of inputs align with the number of outputs
