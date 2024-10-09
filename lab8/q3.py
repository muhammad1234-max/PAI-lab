import numpy as np

even_arr = np.arange(2,20,2).reshape(3,3)
mult = even_arr * 4
identity = np.eye(3)
ans = np.multiply(mult,identity)

print(ans)
