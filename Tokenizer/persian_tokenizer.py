from __future__ import unicode_literals
from hazm import *
import os

# from nltk.corpus import stopwords
# sw = set(stopwords.words('english'))
# print(sw)

punctuations = "#$%&'()*+,-./:;<=>?@[\]^\"_`{|}~]"


def read_from_file():
    address_of_file = os.path.dirname(__file__) + str('/../Data/Persian.xml')
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
                    "title": english_tokenize(row[0]),
                    "content": english_tokenize(row[1])
                })
                # print(f'\t{row[0]} \n{row[1]}')
                line_count += 1
        # print(f'Processed {line_count} lines.')
        return data


def english_tokenize(sentence):
    sentence = "".join([w for w in sentence if w not in punctuations])
    word_tokenized = word_tokenize(sentence)
    lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
    stemmed = [st.stem(word) for word in lemmatized]
    return stemmed


def add_doc():
    pass


data = read_from_file()

print(
    data[0], '\n',
    data[1]
)