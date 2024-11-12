import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

csv_path = "/heart_disease_dataset.csv"  
df = pd.read_csv(csv_path)

df[['Mean', 'Standard Deviation']] = df['Mean ± Standard deviation'].str.split(' ± ', expand=True).astype(float)


np.random.seed(42)


sns.set(style="whitegrid")
fig, axes = plt.subplots(4, 4, figsize=(20, 20))  
fig.suptitle('Seaborn Histograms of Heart Disease Dataset Features', fontsize=20)

axes = axes.flatten()


for i, column in enumerate(df["Feature code"]):
    mean = df["Mean"][i]
    std = df["Standard Deviation"][i]

    
    data = np.random.normal(mean, std, 1000)

    
    sns.histplot(data, bins=20, kde=True, ax=axes[i], color='blue', edgecolor='black')
    axes[i].set_title(column, fontsize=14)
    axes[i].set_xlabel('Value', fontsize=12)
    axes[i].set_ylabel('Frequency', fontsize=12)


plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("seaborn_heart_disease_histograms.png")
