# SQuAD-Fill-in-the-Blanks

This repo provides a corpus of fill-in-the-blank questions derived from the Stanford Question and Answer Dataset (SQuAD): https://rajpurkar.github.io/SQuAD-explorer/

Some statistics:
- Total number of articles = 477
- Mean blanks per article = 256 for train.json; 309 per dev.json
- Percentage of words that are blanked = 4.4% for train.json; 6.2% for dev.json

Used for training fill-in-the-blank classifiers (for example, https://github.com/davestanley/mindpocket)

# Getting started

As with the original SQuAD dataset, there are two json files, `data/train.json` and `data/dev.json`. These have the same structure as the original SQuAD dataset, but each paragraph has two new keys: 

- `context_blanked` - A version of the original contex with key words blanked out
- `blank_classification` - A contains 1 if word should be blanked, 0 if not

# Algorithm

Approach: Use SQuAD's Q&A pairs to identify candidate blank words in the original text. 
1. Remove stopwords from all answers
1. Identified all answers that are less than 2 words (after removal of stopwords)
1. For each of the above answers, blanked out all of these answer words in the corresponding text

This is illustrated schematically below:
![Algorithm Diagram](https://github.com/davestanley/SQuAD-Fill-in-the-Blanks/raw/master/algorithm_diagram.png)

# Example

For further details, see [data_exploration.ipynb](https://github.com/davestanley/SQuAD-Fill-in-the-Blanks/blob/master/data_exploration.ipynb). But, briefly, browsing the data:
 - `arts[442]['paragraphs'][0]['context_blanked']` contains:
>> The Normans ( Norman : Nourmands ; French : Normands ; Latin : Normanni ) were the people who in the ______ and 11th centuries gave their name to Normandy , a region in ______ . They were descended from Norse ( " Norman " comes from " Norseman " ) raiders and pirates from Denmark , Iceland and Norway who , under their leader ______ , agreed to swear fealty to King Charles III of West Francia . Through generations of assimilation and mixing with the native Frankish and Roman - Gaulish populations , their descendants would gradually merge with the Carolingian - based cultures of West Francia . The distinct cultural and ethnic identity of the Normans emerged initially in the first half of the ______ ______ , and it continued to evolve over the succeeding centuries .

- `arts[442]['paragraphs'][0]['blank_classification']` contains:
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Running the algorithm

To re-generate a new train.json and dev.json, run the following:

- `python SQuAD2blanks.py`      # Generates json files containing just the blanks in data/SQuAD_pp_trainingblanks
- `python mergeBlanks.py`       # Merges the classified blanks back into the full dataset


## Dependencies
- Natural Language Toolkit (nltk) (for detecting stopwords)



