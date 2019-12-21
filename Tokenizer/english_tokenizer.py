from __future__ import unicode_literals
# import nltk
#
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# if there was any problem with NLTK, uncomment the line above
from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import WordNetLemmatizer
import os
import csv


# from nltk.corpus import stopwords
# sw = set(stopwords.words('english'))
# print(sw)

def analyser(sentence, stem=True):
    # get a sentence. returns a list of words
    punctuations = "\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"
    st = LancasterStemmer()
    wnl = WordNetLemmatizer()
    s = ""
    for w in sentence:
        if w not in punctuations:
            s += w
        else:
            s += " "
    sentence = s
    if stem is False:
        sentence = "".join([w.lower() if w.isupper() else w for w in sentence])
        words = word_tokenize(sentence)
        lemmatized = [wnl.lemmatize(word) for word in words]
        return lemmatized
    else:
        words = word_tokenize(sentence)
        lemmatized = [wnl.lemmatize(word) for word in words]
        stemmed = [st.stem(word) for word in lemmatized]
        return stemmed


class DataSet:
    def __init__(self, address_of_file, has_tag=False):
        # list of dictionaries:
        self.read_from_file(address_of_file, has_tag)
        # gives self.raw_data
        self.data = self.get_data(has_tag)
        self.not_stemmed_data = self.get_data(stem=False)

    # not_stemmed_data = get_not_stemmed_data()

    def get_value_by_id(self, index, key):
        index = index - 1
        raw_datum = self.raw_data[index]
        return raw_datum[key]

    def read_from_file(self, address_of_file, has_tag=False):
        # address_of_file = os.path.dirname(__file__) + str('/../Data/English.csv')
        with open(address_of_file) as english_raw_dataset:
            csv_reader = csv.reader(english_raw_dataset)
            self.raw_data = []
            line_count = 0
            if not has_tag:
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        self.raw_data.append(
                            {
                                "id": line_count,
                                "title": row[0],
                                "content": row[1]
                            })
                        line_count += 1
                print(f'Processed {line_count} lines of raw data.')
            else:
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        self.raw_data.append(
                            {
                                "id": line_count,
                                "tag": row[0],
                                "title": row[1],
                                "content": row[2]
                            })
                        line_count += 1
                print(f'Processed {line_count} lines of raw data.')

    def get_data(self, stem=True, has_tag=False):
        raw_data = self.raw_data
        data = []
        if not has_tag:
            if stem is False:
                for datum in raw_data:
                    data.append(
                        {
                            "id": datum['id'],
                            "title": analyser(datum['title'], stem=False),
                            "content": analyser(datum['content'], stem=False)
                        })
            else:
                for datum in raw_data:
                    data.append(
                        {
                            "id": datum['id'],
                            "title": analyser(datum['title']),
                            "content": analyser(datum['content'])
                        })
        else:
            if stem is False:
                for datum in raw_data:
                    data.append(
                        {
                            "id": datum['id'],
                            "title": analyser(datum['title'], stem=False),
                            "content": analyser(datum['content'], stem=False),
                            "tag": analyser(datum['tag'], stem=False)
                        })
            else:
                for datum in raw_data:
                    data.append(
                        {
                            "id": datum['id'],
                            "title": analyser(datum['title']),
                            "content": analyser(datum['content']),
                            "tag": analyser(datum['tag'])
                        })
        return data


# dataSet = DataSet()
