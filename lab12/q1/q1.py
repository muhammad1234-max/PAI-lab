import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#Load the datasets
data = pd.read_csv("housing.csv")

#preview the data
print("Data Head:")
print(data.head())

#check for null values and drop them for simplicity (data cleaning)
if data.isnull().sum().any():
    print("Null values detected, dropping rows with nulls.")
    data.dropna(inplace=True)

#assuming numerical columns are suitable for clustering
numerical_columns = data.select_dtypes(include='number').columns
print(f"Numerical columns for clustering: {numerical_columns}")

#standardizing the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[numerical_columns])

#determine the optimal number of clusters using the elbow curve graph
inertia = []
cluster_range = range(1, 11)  #testing for 1-10 clusters
for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data) #fitting k-means algorithm 
    inertia.append(kmeans.inertia_) #adding inertia value to list of inertia of all cluster

#plot the elbow curve
plt.figure(figsize=(8, 6))
plt.plot(cluster_range, inertia, marker='o', linestyle='--')
plt.title('Elbow Curve for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.xticks(cluster_range)
plt.grid()
plt.show()

#based on the elbow curve, pick the optimal number of clusters 
optimal_clusters = 5  #observed this from the above graph

#apply K-Means
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_data)

#save the clustered dataset
data.to_csv("data.csv", index=False)

print(f"Clustering completed. Clustered data saved to data.csv .")
