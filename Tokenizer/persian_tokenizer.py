from __future__ import unicode_literals
from hazm import *
import os
from string import punctuation


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


def persian_tokenize(data):
    for datum in data:
        datum['content'] = "".join([w for w in datum['content'] if w not in punctuation])
        word_tokenized = word_tokenize((datum['content']))
        lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
        stemmed = [st.stem(word) for word in lemmatized]
        datum['content'] = stemmed
        datum['title'] = "".join([w for w in datum['title'] if w not in punctuation])
        word_tokenized = word_tokenize((datum['title']))
        lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
        stemmed = [st.stem(word) for word in lemmatized]
        datum['title'] = stemmed
    return data


def add_doc():
    pass


# data = read_from_file()
# data = persian_tokenize(data)
# print(
#     data[0], '\n',
#     data[1]
# )
