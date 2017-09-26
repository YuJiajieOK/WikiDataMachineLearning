import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation,svm, tree
import ast

with open('Collected - Copy.txt') as C:
    for o in C:
        o = ast.literal_eval(o)
with open('labels - Copy.txt') as L:
    for l in L:
        l = ast.literal_eval(l)

for i in range(len(o)):
    o[i].remove(o[i][0])


X = np.array(o)
# X = preprocessing.scale(X)
print(len(o))
Y = np.array(l)
print(len(l))

X_train, X_test,Y_train,Y_test = cross_validation.train_test_split(X,Y,test_size=0.2)

# Classifier = LinearRegression()
# Classifier = svm.SVR()
Classifier = tree.DecisionTreeClassifier()
Classifier.fit(X_train,Y_train)
accuracy = Classifier.score(X_test,Y_test)

print(accuracy)

