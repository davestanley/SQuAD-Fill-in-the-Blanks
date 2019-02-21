# SQuAD-Fill-in-the-Blanks

Fill-in-the-blank questions derived from the Stanford Question and Answer Dataset (SQuAD): https://rajpurkar.github.io/SQuAD-explorer/


For training fill-in-the-blank classifiers (for example, https://github.com/davestanley/mindpocket)

# Getting started

As with the original SQuAD dataset, there are two json files, `data/train.json` and `data/dev.json`. These have the same structure as the original SQuAD dataset, but each paragraph has two new keys: 

- `context_blanked` - A version of the original contex with key words blanked out
- `blank_classification` - A contains 1 if word should be blanked, 0 if not


# How it works

I used the following approach to generate fill-in-the-blank questions from the SQuAD Q&A
1. Removed stopwords from all answers
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
