import numpy as np 

options = [2,5,9,10]

random = np.random.choice(options, size=(4,4)) #matrix with random numbers only from given options
identity_matrix = np.eye(4) 
multiplied = np.dot(random,identity_matrix)
odd_matrix = np.arange(1,32,2).reshape(4,4) #matrix with first 16 odd numbers

ans = multiplied + odd_matrix
print(ans)
