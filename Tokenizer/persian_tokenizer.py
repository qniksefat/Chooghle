from __future__ import unicode_literals
#import nltk
#nltk.download('punkt')
from nltk import word_tokenize, sent_tokenize
import csv

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
e_tokens = word_tokenize(sentence)
print(e_tokens)


def read_from_file():
    with open('/home/qasem/PycharmProjects/mir/Chooghle/Data/English.csv') as english_raw_dataset:
        print("im here in reader")
        csv_reader = csv.reader(english_raw_dataset)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)} \n\n')
                line_count += 1
            elif line_count < 2:
                print(f'\t{row[0]} \n{row[1]}')
                line_count += 1
        print(f'Processed {line_count} lines.')

def english_tokenizer():
    pass

read_from_file()
