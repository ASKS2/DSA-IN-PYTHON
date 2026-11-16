import numpy as np
print(np.eye(3))
# this will print a 3x3 identity matrix, consisting of 1s 
# on the diagonal and 0s elsewhere.

print(np.eye(3, k=1) )
# this will print a 3x3 matrix with 1s on the first 
# superdiagonal (just above the main diagonal) and 0s 
# elsewhere. The k parameter specifies the diagonal to
#  fill with 1s, where k=0 is the main diagonal, k=1 is 
# the first superdiagonal, and k=-1 is the first 
# subdiagonal.


np.random.seed(42)                   # makes results repeatable
np.random.rand(2, 3)                 # uniform floats in [0, 1), shape 2x3
np.random.randn(2, 3)                # standard normal (mean 0, std 1)
np.random.randint(1, 10, size=(2, 3)) # integers 1..9 (10 excluded)
np.random.choice([10, 20, 30], size=5)   # random picks with replacement

# Converting back to a Python list
np.array([[1, 2], [3, 4]]).tolist()   # [[1, 2], [3, 4]]


f = np.array([1.7, 2.9, -3.2])
f.astype(int)            # [ 1  2 -3]   truncates toward zero, does NOT round
np.round(f).astype(int)  # [ 2  3 -3]   round first if you want rounding

s = np.array(['1', '2', '3'])
s.astype(int)            # [1 2 3]      strings to numbers