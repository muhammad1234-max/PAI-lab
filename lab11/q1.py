import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#all scikit models that would be used in the program
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("heart_disease.csv")
x= df.drop('target',axis=1) #getting all the features or the independent variables
y = df['target'] #getting the target or the depending variable that we will be using the ML algorithm to estimate

#splitting the data into training set which is used for training the model
#testing sets which is used to evaluate the data like to calculate accuracy and all
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.3,random_state=42)

neighbor_range = range(1,251) #represents a potential value for k
accuracies = [] #to score the accuracy values for each value of k

#train and evaluate model for each neighbour count
for k in neighbor_range:
    knn = KNeighborsClassifier(n_neighbors=k) #initializing a KNN classifier with K neighbours and will consider k neighbours when making the prediction
    knn.fit(X_train,Y_train) #trains the model on the training data
    y_pred = knn.predict(X_test) #predicted values of the target parameter based on the trained model
    accuracies.append(accuracy_score(Y_test,y_pred)) #calculates accuracy comparing predicted values to true labels or test data
    
max_accuracy = max(accuracies)
min_accuracy = min(accuracies)
best_k = [neighbor_range[i] for i, acc in enumerate(accuracies) if acc == max_accuracy] #list of k values with the highest accuracy
worst_k = [neighbor_range[i] for i, acc in enumerate(accuracies) if acc == min_accuracy] #list of k values with lowest accuracy

print(f"Highest accuracy: {max_accuracy} achieved at k = {best_k}")
print(f"Lowest accuracy: {min_accuracy} achieved at k = {worst_k}")

#plotting results
plt.figure(figsize=(10, 6))
plt.plot(neighbor_range, accuracies, color='b', marker='o', markerfacecolor='r')
plt.title('Accuracy vs. Number of Neighbors')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.show()
