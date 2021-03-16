from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

def challenge2():
    iris_dataset = pd.read_csv('iris.data', names=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'type'])
    forest_classifier = RandomForestClassifier(n_estimators=100)

    type = iris_dataset['type']

    input = iris_dataset.drop("type", axis=1)

    input_test, input_train, type_test, type_train = train_test_split(input, type, test_size=.25)

    forest_classifier.fit(input_train, type_train)

    prediction = forest_classifier.predict(input_test)

    file = open('RandomForestClassifier_Results.txt', 'w')

    file.write("Accuracy: ")
    file.write(str(metrics.accuracy_score(type_test, prediction)))
    file.write("\n Confusion Matrix: \n")
    file.write(str(metrics.confusion_matrix(type_test, prediction)))
