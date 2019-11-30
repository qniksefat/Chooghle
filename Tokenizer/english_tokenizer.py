# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# if there was any problem with NLTK, uncomment the line above
from __future__ import unicode_literals
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import os
import csv

# from nltk.corpus import stopwords
# sw = set(stopwords.words('english'))
# print(sw)
punctuations = "\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"
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
            else:
                # "else" to process whole file
                data.append(
                {
                    "id": line_count,
                    "title": english_tokenize(row[0]),
                    "content": english_tokenize(row[1])
                })
                # print(f'\t{row[0]} \n{row[1]}')
                line_count += 1
        print(f'Processed {line_count} lines of csv data.')
        return data


def get_raw_data():
    address_of_file = os.path.dirname(__file__) + str('/../Data/English.csv')
    with open(address_of_file) as english_raw_dataset:
        csv_reader = csv.reader(english_raw_dataset)
        data = []
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                data.append(
                {
                    "id": line_count,
                    "title": row[0],
                    "content": row[1]
                })
                line_count += 1
        print(f'And processed {line_count} lines of raw data.')
        return data

def get_not_stemmed_data():
    address_of_file = os.path.dirname(__file__) + str('/../Data/English.csv')
    with open(address_of_file) as english_raw_dataset:
        csv_reader = csv.reader(english_raw_dataset)
        data = []
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)} \n\n')
                line_count += 1
            else:
                # "else" to process whole file
                data.append(
                {
                    "id": line_count,
                    "title": english_tokenize_not_stemmed(row[0]),
                    "content": english_tokenize_not_stemmed(row[1])
                })
                # print(f'\t{row[0]} \n{row[1]}')
                line_count += 1
        print(f'Processed {line_count} lines of csv data.')
        return data


def english_tokenize(sentence):
    s = ""
    for w in sentence:
        if w not in punctuations:
            s += w
        else:
            s += " "
    sentence = s
    word_tokenized = word_tokenize(sentence)
    lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
    stemmed = [st.stem(word) for word in lemmatized]
    return stemmed

def english_tokenize_not_stemmed(sentence):
    s = ""
    for w in sentence:
        if w not in punctuations:
            s += w
        else:
            s += " "
    sentence = s
    word_tokenized = word_tokenize(sentence)
    lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
    return lemmatized


class DataSet:
    data = read_from_file()
    raw_data = get_raw_data()
    not_stemmed_data = get_not_stemmed_data()

    def get_value_by_id(self, index, key):
        index = index - 1
        raw_datum = self.raw_data[index]
        return raw_datum.get(key)


dataSet = DataSet()
