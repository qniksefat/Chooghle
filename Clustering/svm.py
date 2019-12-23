from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from sklearn.svm import SVC
import os

test_data = pd.read_csv(os.path.join('data', 'test_data_with_train_dictionary.csv'))
x_test = test_data.drop(['documents_size', 'tag.1'], axis=1)
y_test = test_data[['tag.1']]

train_data = pd.read_csv(os.path.join('data', 'train_data.csv'))
x_train = train_data.drop('tag.1', axis=1)
y_train = train_data[['tag.1']]

# sv_classifier = SVC(kernel='sigmoid')
# sv_classifier = SVC(kernel='rbf')
# sv_classifier = SVC(kernel='poly', degree=8)
### You can input C in the SVC
sv_classifier = SVC(kernel='linear')
sv_classifier.fit(x_train, y_train)
y_predicted = sv_classifier.predict(x_test)

print("SVM results:")
print(confusion_matrix(y_test, y_predicted))
print(classification_report(y_test, y_predicted))
