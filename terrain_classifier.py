import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv('datasets/Crop_recommendation.csv')

X = data.iloc[:, 0:7]
y = data.iloc[:, 7:8]
fn = data.columns[:7].values

X_train, X_test, y_train, y_test = train_test_split(X, np.ravel(y), test_size=0.3, random_state=42)

clf = RandomForestClassifier(max_depth=7, random_state=10)

clf.fit(X_train, y_train)
