import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sb

def print_hist_features(ds):
      all_columns = ds.columns[:-1]
      plt.figure(figsize=(15,13))
      i = 1
      for column in all_columns[:]:
            plt.subplot(3,3,i)
            sb.histplot(data[column])
            i+=1
      plt.show()


if __name__ == '__main__':
    data = pd.read_csv('datasets/Crop_recommendation.csv')
    
    #Dataset label distribution
    histogram = data['label'].value_counts()
    plt.bar(histogram.to_dict().keys(), histogram.to_dict().values(), 0.7)
    plt.xticks(rotation=-90)
    plt.show()

    #Feature variance
    print_hist_features(data)

    #Features vs Crop
    #Rainfall
    sb.scatterplot(data=data, y="label", x="rainfall", hue="label")
    plt.title("Rainfall vs Crop")
    plt.show()

    #Humidity
    sb.scatterplot(data=data, y="label", x="humidity", hue="label")
    plt.title("Humidity vs Crop")
    plt.show()

    #N
    sb.scatterplot(data=data, y="label", x="N", hue="label")
    plt.title("Nitrogen vs Crop")
    plt.show()

    #P
    sb.scatterplot(data=data, y="label", x="P", hue="label")
    plt.title("Phosphorus  vs Crop")
    plt.show()

    #K
    sb.scatterplot(data=data, y="label", x="K", hue="label")
    plt.title("Potassium  vs Crop")
    plt.show()

    #pH
    sb.scatterplot(data=data, y="label", x="ph", hue="label")
    plt.title("pH  vs Crop")
    plt.show()

    #Temperature
    sb.scatterplot(data=data, y="label", x="temperature", hue="label")
    plt.title("Temperature  vs Crop")
    plt.show()

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

    # Random forest(Depth 3) Metrics
    clf = RandomForestClassifier(max_depth=3, random_state=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    depth3_accuracy = round(accuracy_score(y_test, predictions), 2)
    depth3_precision = round(precision_score(y_test, predictions, average="macro", zero_division=1), 2)
    depth3_recall = round(recall_score(y_test, predictions, average="macro"), 2)
    depth3_error_rate = np.mean(predictions != y_test)

    # Random forest(Depth 7) Metrics
    clf = RandomForestClassifier(max_depth=7, random_state=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    depth7_accuracy = round(accuracy_score(y_test, predictions), 2)
    depth7_precision = round(precision_score(y_test, predictions, average="macro", zero_division=1), 2)
    depth7_recall = round(recall_score(y_test, predictions, average="macro"), 2)
    depth7_error_rate = np.mean(predictions != y_test)

    # Random forest(Depth 13) Metrics
    clf = RandomForestClassifier(max_depth=13, random_state=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    depth13_accuracy = round(accuracy_score(y_test, predictions), 2)
    depth13_precision = round(precision_score(y_test, predictions, average="macro", zero_division=1), 2)
    depth13_recall = round(recall_score(y_test, predictions, average="macro"), 2)
    depth13_error_rate = np.mean(predictions != y_test)

    # Depth VS [Accuracy - Precision - Recall - Error Rate]
    results = pd.DataFrame.from_dict({
        'Depth=3': [depth3_accuracy, depth3_precision, depth3_recall, depth3_error_rate],
        'Depth=7': [depth7_accuracy, depth7_precision, depth7_recall, depth7_error_rate],
        'Depth=13': [depth13_accuracy, depth13_precision, depth13_recall, depth13_error_rate],
    },
        orient='index', columns=['Accuracy', 'Precision', 'Recall', 'Error Rate'])

    print(results)

    # Accuracy VS Depth Random forest Plot
    accuracy = []
    for i in range(1, 16):
        clf = RandomForestClassifier(max_depth=i, random_state=10)
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        accuracy.append(accuracy_score(y_test, predictions))

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 16), accuracy, color='blue', linestyle='solid',
             marker='.', markerfacecolor='blue', markersize=10)
    plt.title('Accuracy vs. Random Forest Depth')
    plt.xlabel('Depth')
    plt.ylabel('Accuracy')

    plt.show()
    print()

    # Random Forest Depth=7 Results
    clf = RandomForestClassifier(max_depth=7, random_state=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("Random Forest(Depth=7) Results:\n" + classification_report(y_test, predictions))

    # KNN Results (K = 3)
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X, np.ravel(y))
    predictionsKNN = neigh.predict(X_test)
    print("Knn Results (K = 3):\n" + classification_report(y_test, predictionsKNN))
