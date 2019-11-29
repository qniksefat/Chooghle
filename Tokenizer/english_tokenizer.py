from __future__ import unicode_literals
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# if there was any problem with NLTK, uncomment the line above
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import os
import csv
from nltk.stem import WordNetLemmatizer

from Tokenizer import foo_func
foo_func.foo()

st = LancasterStemmer()
wnl = WordNetLemmatizer()


def read_from_file():
    address_of_file = os.path.dirname(__file__) + str('/../Data/English.csv')
    with open(address_of_file) as english_raw_dataset:
        csv_reader = csv.reader(english_raw_dataset)
        data = []
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)} \n\n')
                line_count += 1
            elif line_count < 3:
                # "else" to process whole file
                data.append(
                {
                    "id": line_count,
                    "title": row[0],
                    "content": row[1]
                })
                # print(f'\t{row[0]} \n{row[1]}')
                line_count += 1
        print(f'Processed {line_count} lines.')
        return data


def english_tokenize(data):
    for datum in data:
        word_tokenized = word_tokenize((datum['content']))
        lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
        stemmed = [st.stem(word) for word in lemmatized]
        datum['content'] = stemmed
        word_tokenized = word_tokenize((datum['title']))
        lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
        stemmed = [st.stem(word) for word in lemmatized]
        datum['title'] = stemmed
    return data


def add_doc():
    pass


data = read_from_file()
data = english_tokenize(data)
print(
    data[0], '\n',
    data[1]
)
