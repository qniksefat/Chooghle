from __future__ import unicode_literals
from hazm import *
import os


from xml.dom import minidom

address_of_file = os.path.dirname(__file__) + str('/../Data/small_part.xml')
mydoc = minidom.parse(address_of_file)

pages = mydoc.getElementsByTagName('page')
# # one specific item attribute
print("pages 0")
print(pages[0]['title'])
print(pages[0].attributes['title'].value)
#
# # all item attributes
# print('\nAll attributes:')
# for elem in items:
#     print(elem.attributes['name'].value)
#
# # one specific item's data
# print('\nItem #2 data:')
# print(items[1].firstChild.data)
# print(items[1].childNodes[0].data)
#
# # all items data
# print('\nAll item data:')
# for elem in items:
#     print(elem.firstChild.data)


punctuations = "\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"


# def read_from_file():
#     address_of_file = os.path.dirname(__file__) + str('/../Data/Persian.xml')
#     with open(address_of_file) as english_raw_dataset:
#         csv_reader = csv.reader(english_raw_dataset)
#         data = []
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 # print(f'Column names are {", ".join(row)} \n\n')
#                 line_count += 1
#             else:
#                 # "else" to process whole file
#                 data.append(
#                 {
#                     "id": line_count,
#                     "title": english_tokenize(row[0]),
#                     "content": english_tokenize(row[1])
#                 })
#                 # print(f'\t{row[0]} \n{row[1]}')
#                 line_count += 1
#         print(f'Processed {line_count} lines of csv data.')
#         return data
#
#
# def get_raw_data():
#     address_of_file = os.path.dirname(__file__) + str('/../Data/Persian.xml')
#     with open(address_of_file) as english_raw_dataset:
#         csv_reader = csv.reader(english_raw_dataset)
#         data = []
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 line_count += 1
#             else:
#                 data.append(
#                 {
#                     "id": line_count,
#                     "title": row[0],
#                     "content": row[1]
#                 })
#                 line_count += 1
#         print(f'And processed {line_count} lines of raw data.')
#         return data
#
#
# def english_tokenize(sentence):
#     sentence = "".join([w for w in sentence if w not in punctuations])
#     word_tokenized = word_tokenize(sentence)
#     lemmatized = [wnl.lemmatize(word) for word in word_tokenized]
#     stemmed = [st.stem(word) for word in lemmatized]
#     return stemmed


class DataSet:
    pass
    # data = read_from_file()
    # raw_data = get_raw_data()
    #
    # def get_value_by_id(self, index, key):
    #     index = index - 1
    #     raw_datum = self.raw_data[index]
    #     return raw_datum.get(key)


# dataSet = DataSet()

# data = read_from_file()
# data = persian_tokenize(data)
# print(
#     data[0], '\n',
#     data[1]
# )
