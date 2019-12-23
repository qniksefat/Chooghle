import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os

# data = pd.read_csv('../SVM/data/test_data_with_train_dictionary.csv')
# x = data.drop(['tag.1', 'documents_size'], axis=1)
# y = data[['tag.1']]
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

test_data = pd.read_csv(os.path.join('data', 'test_data_with_train_dictionary.csv'))
x_test = test_data.drop(['documents_size', 'tag.1'], axis=1)
y_test = test_data[['tag.1']]

train_data = pd.read_csv(os.path.join('data', 'train_data.csv'))
x_train = train_data.drop('tag.1', axis=1)
y_train = train_data[['tag.1']]

clf = RandomForestClassifier(n_estimators=200)
clf.fit(x_train, y_train.values.ravel())

y_predicted = clf.predict(x_test)

print("Random Forest results:")
print(confusion_matrix(y_test, y_predicted))
print(classification_report(y_test, y_predicted))
