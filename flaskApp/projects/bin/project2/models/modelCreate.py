import numpy as np
import pandas as pd

df = pd.read_csv('../data/diabetes.csv')

x = df.iloc[:, :-1]
y = df.iloc[:, -1]
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn.pipeline import Pipeline
pipe = Pipeline([('min_max', MinMaxScaler()), ('standard', StandardScaler())])

x_finall = pipe.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_finall, y)

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

rn = RandomForestClassifier(n_estimators=100, max_depth=7)
rn.fit(x_train, y_train)

print(rn.score(x_train, y_train))

predict = rn.predict(x_test)
print("accuracy_score For Test ",accuracy_score(y_test, predict))

print(confusion_matrix(predict, y_test))

import pickle

# save the model to disk
filename = 'pipeMinSc_StdSc.pkl'
filename1 = 'RFClr.pkl'
pickle.dump(pipe, open(filename, 'wb'))
pickle.dump(rn, open(filename1, 'wb'))
print("Model Save Successful")
