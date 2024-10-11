import numpy as np

random_array = np.random.rand(1000)

avg = np.mean(random_array)
variance = np.var(random_array)
std_dev = np.std(random_array)

results = f"Average:{avg}\nVariance:{variance}\nStandard Deviation:{std_dev}"

with open("statistics_data.txt",'w') as file:
    file.write(results)
    
print("results saved to file")
