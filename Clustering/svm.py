from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from sklearn.svm import SVC
import os

from sklearn.model_selection import train_test_split
data = pd.read_csv(os.path.join('..', 'Data', 'test_data_with_train_dictionary.csv'))
x = data.drop(['tag.1', 'documents_size'], axis=1)
y = data[['tag.1']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

test_data = pd.read_csv(os.path.join('..', 'Data', 'test_data_with_train_dictionary.csv'))
# x_test = test_data.drop(['documents_size', 'tag.1'], axis=1)
# y_test = test_data[['tag.1']]
#
train_data = pd.read_csv(os.path.join('..', 'Data', 'train_data.csv'))
# x_train = train_data.drop('tag.1', axis=1)
# y_train = train_data[['tag.1']]

# other kernels!
# sv_classifier = SVC(kernel='sigmoid')
# sv_classifier = SVC(kernel='rbf')
# sv_classifier = SVC(kernel='poly', degree=8)

C = input("Please enter C value:")
sv_classifier = SVC(kernel='linear', C=C)
sv_classifier.fit(x_train, y_train.values.ravel())
y_predicted = sv_classifier.predict(x_test)


# we used 10% of data for local and whole data on Google CoLab
print("SVM results:")
print(confusion_matrix(y_test, y_predicted))
print(classification_report(y_test, y_predicted))
