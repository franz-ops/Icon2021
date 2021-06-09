import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('datasets/Crop_recommendation.csv')

    X = data.iloc[:, 0:7]
    y = data.iloc[:, 7:8]
    fn = data.columns[:7].values
    cn = ["rice",
          "banana",
          "watermelon",
          "blackgram",
          "chickpea",
          "pigeonpeas",
          "papaya",
          "cotton",
          "jute",
          "mungbean",
          "apple",
          "pomegranate",
          "muskmelon",
          "maize",
          "lentil",
          "mothbeans",
          "mango",
          "coconut",
          "coffee",
          "orange",
          "grapes",
          "kidneybeans"]

    X_train, X_test, y_train, y_test = train_test_split(X, np.ravel(y), test_size=0.3, random_state=42)

    clf = RandomForestClassifier(max_depth=7, random_state=10)
    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)

    print(classification_report(y_test, predictions))

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=800)
    tree.plot_tree(clf.estimators_[0],
                   feature_names=fn,
                   class_names=cn,
                   filled=True);
    fig.savefig('rf_individualtree.png')
