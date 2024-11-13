import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#load dataset into a dataframe
df = pd.read_csv('heart_disease.csv')
X = df.drop('target', axis=1) #independent feature variables
y = df['target'] #target dependent variable that will be predicted

#initialize variables
neighbor_range = range(1, 251)  #range of k values to test
all_accuracies = {}  #dictionary to store accuracies for each seed

#loop over random seeds from 1 to 10
for seed in range(1, 11):  
    # Split data into training and testing sets with the current seed
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)
    
    accuracies = []  #list to store accuracies for the current seed
    
    #train and evaluate model for each neighbor count
    for k in neighbor_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)
    
    #store accuracies for the current seed
    all_accuracies[seed] = accuracies
    print(f"Accuracies for random seed {seed}: {accuracies}")

#calculate the overall highest and lowest accuracy values and corresponding k values
max_accuracy = max(max(accuracies) for accuracies in all_accuracies.values())
min_accuracy = min(min(accuracies) for accuracies in all_accuracies.values())


best_seed, best_k = None, None
worst_seed, worst_k = None, None

for seed, accuracies in all_accuracies.items():
    if max_accuracy in accuracies:
        best_seed = seed
        best_k = neighbor_range[accuracies.index(max_accuracy)]
    if min_accuracy in accuracies:
        worst_seed = seed
        worst_k = neighbor_range[accuracies.index(min_accuracy)]

print(f"Highest accuracy: {max_accuracy} achieved at seed = {best_seed}, k = {best_k}")
print(f"Lowest accuracy: {min_accuracy} achieved at seed = {worst_seed}, k = {worst_k}")
