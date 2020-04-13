
import numpy as np
import pandas as pd
import csv
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os



X = df.iloc[:, 1:785].values
y = df.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,random_state=42, stratify=y)



scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)


knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)


df = pd.read_csv(TEST)
TX = df.iloc[:, 0:784].values


scaler = StandardScaler()

scaler.fit(TX)
TX = scaler.transform(TX)

result = knn.predict(TX)



with open(resultcsv, 'w', newline='') as csvfile:
    fieldnames = ['wifi', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, item in enumerate(result):
        writer.writerow({'wifi': str(i+1), 'Label': str(item)})
       
print("out")


print("find best k")

best_score = 0.0
best_k = -1
for k in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
   

    if score > best_score:
        print(best_k, best_score)
        best_k = k
        best_score = score
    print("score , k , best score, best k")
    print(score)
    print(k)
    print(best_score)
    print(best_k)
print("found best k")
print(best_k, best_score)

print("DONE")


print("knn = 3 ")
knn = KNeighborsClassifier(n_neighbors = 3)
print("fiting")
knn.fit(X_train, y_train)
print("score")
score = knn.score(X_test, y_test)
print(score)

print("done")


print("scaler")

scaler = StandardScaler()
print("fit")
scaler.fit(X_train)
X_train = scaler.transform(X_train)
print("fiting knn")
knn.fit(X_train, y_train)
print("finding  score")

score = knn.score(X_test, y_test)
print(score)



