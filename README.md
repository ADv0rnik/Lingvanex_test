### Text filtering

#### Background 
The current functionality of the application is based on OpusFilter toolkit: https://github.com/Helsinki-NLP/OpusFilter 
it is possible to use an overal OpusFilter functionality together with selfwritten filter and preprocessing classes. 
<p>Some custom modules included to this project:</p>

*TenWordsLengthFilter* - specific filter to delete all sentences longer than 10 words from provided text. The filter was tested on Ubuntu 22.04 OS

*StringCleaner* - custom preprocessing class based on regex to clean string from existing "garbage" e.g. quotes, extra terminal dots etc.

*UnicodeCleaner* - custom preprocessing class which helps to remove unprintable characters and left only ASCII printable characters

#### Usage
Before using this filter make sure that opusfilter is preinstalled on your local machine. Then follow these steps:
1. Clone the repository onto your local machine by following command:
   
    `git clone https://github.com/ADv0rnik/Lingvanex_test.git` or if you are using ssh

    `git clone git@github.com:ADv0rnik/Lingvanex_test.git`

2. Create virtual environment by using:
`python -m venv venv` or `virtualen venv`
3. Set up configuration
   - Set up your `config.yml` file (if you are going to run opusfilter with CONFIG flag). Check this [page](https://helsinki-nlp.github.io/OpusFilter/usage.html) for more details.
   - Alternatively, set up `config.json` file according to existing example
4. From root directory run `source aliases` to be able to use short commands (please, see below)
5. Add the directory that contains custom modules to PYTHONPATH environment variable by using the following command from the terminal:
    ```commandline
    export PYTHONPATH="${PYTHONPATH}:/path/to/your/module/"
    ```
    or
   ```commandline
   update_pythonpath
   ```
6. Once the `config.json` set up run the following command from the terminal:
   ```commandline
   run_opus
   ```
7. To run a single step use the following command (assuming that input files exist). Check this [page](https://helsinki-nlp.github.io/OpusFilter/usage.html) for more details.
    ```commandline
    opusfilter-cmd filter --inputs WikiMatrix.en-ru.en WikiMatrix.en-ru.ru --outputs text_f.en-ru.en text_f.en-ru.ru --filters '[{"TenWordsLengthFilter": {"max_length": 10}, "module": "len_filter"}]'
    ```

#### Tests
To run some tests after text cleaning use
```python
python3 -m unittest tests
```

#### Troubleshooting
Some possible issues:<br>

**1. Module not found**<br>

*Solution*: Make sure that you added filter module to PYTHONPATH environment variable. Check it with Python `sys` module

```python
import sys
print(sys.path)
```

**2. opusfilter.ConfigurationError: Number of input and output files should match in sort**

The filter command requires a list of input files as well as the similar number of output files

*Solution*: Make sure that the number of inputs align with the number of outputs
