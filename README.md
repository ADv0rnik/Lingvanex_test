### Text filtering

#### Background 
The current functionality of the application is based on OpusFilter toolkit: https://github.com/Helsinki-NLP/OpusFilter 
it is possible to use an overal OpusFilter functionality together with selfwritten filter classes. 

TenWordsLengthFilter - specific filter to delete all sentences longer than 10 words from provided text. 

#### Usage
Before using this filter make sure that opusfilter is preinstalled on your local machine. Than follow these steps:
1. Clone the repository onto your local machine by following command:
`git clone https://github.com/ADv0rnik/Lingvanex_test.git`
or if you are using ssh
`git clone git@github.com:ADv0rnik/Lingvanex_test.git`
2. Create virtual environment by using:
`python -m venv venv`
3. Setup your `config.yml` file.
4. Run the following command to clean up sample text:
```commandline
opusfilter-cmd filter --inputs text.en-ru.en text.en-ru.ru --outputs text_f.en-ru.en text_f.en-ru.ru --filters '[{"TenWordsLengthFilter": {"max_length": 10}, "module": "len_filter"}]'
```

#### Troubleshooting
