import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Housing.csv")

continuous_features = data[["bedrooms", "price"]]  
categorical_features = data[["basement", "hotwaterheating", "airconditioning"]]  


continuous_features.hist(bins=30, figsize=(10, 5))
plt.suptitle("Distributions of Continuous Features")
plt.show()

plt.figure(figsize=(12, 10))
plotnumber = 1
for column in continuous_features.columns:
    plt.subplot(2, 2, plotnumber)
    sns.boxplot(y=continuous_features[column])
    plt.title(f"Boxplot of {column}")
    plotnumber += 1  

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 10))
for i, column in zip(range(len(continuous_features.columns)), continuous_features.columns):
    plt.subplot(2, 2, i + 1)
    plt.hist(continuous_features[column], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(continuous_features[column].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
    plt.axvline(continuous_features[column].median(), color='green', linestyle='dashed', linewidth=1, label='Median')
    plt.title(f"Overall Histogram of {column}")
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()

plt.suptitle("Overall Distribution of Continuous Features", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

correlation_matrix = continuous_features.corr()
plt.figure(figsize=(6, 3))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title("Correlation Matrix of Continuous Features")
plt.show()

plt.figure(figsize=(12, 6))
for i, column in enumerate(continuous_features.columns, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(x=data['basement'], y=continuous_features[column])
    plt.title(f"{column} Distribution by basement")
    
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for i, column in enumerate(continuous_features.columns, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(x=data['hotwaterheating'], y=continuous_features[column])
    plt.title(f"{column} Distribution by hotwaterheating")
    
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for i, column in enumerate(continuous_features.columns, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(x=data['airconditioning'], y=continuous_features[column])
    plt.title(f"{column} Distribution by airconditioning")

plt.tight_layout()
plt.show()

label = 'price'  

if label in data.columns:
    significant_features = correlation_matrix[label].abs().nlargest(3).index.tolist()  

    plt.figure(figsize=(10, 5))
    for i, feature in enumerate(significant_features[1:], 1):  
        plt.subplot(1, 2, i)
        sns.regplot(x=data[label], y=data[feature], scatter_kws={'alpha': 0.5})
        plt.title(f"{label} vs. {feature} with Regression Line")
        plt.xlabel(label)
        plt.ylabel(feature)

    plt.tight_layout()
    plt.show()
else:
    print("Target variable not found in the dataset.")
