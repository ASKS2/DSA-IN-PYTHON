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


a = np.array([10, 20, 30, 40, 50])
#  index:       0   1   2   3   4
#  negative:  -5  -4  -3  -2  -1

a[0]        # 10   first
a[2]        # 30
a[-1]       # 50   last
a[-2]       # 40   second from last
a[5]        # IndexError: index 5 is out of bounds for axis 0 with size 5

m = np.arange(1, 13).reshape(3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

m[1, 2]      # 7      row 1, column 2
m[0, 0]      # 1
m[-1, -1]    # 12     last row, last column
m[2, 0]      # 9
m[0]         # [1 2 3 4]   a whole row (shape (4,))
m[-1]        # [ 9 10 11 12]
m[1][2]      # 7      works, but m[1, 2] is cleaner and faster

a = np.array([10, 20, 30, 40, 50])
mask = a > 25
mask            # [False False  True  True  True]
a[mask]         # [30 40 50]
a[a > 25]       # [30 40 50]   same, in one line

a[(a > 15) & (a < 45)]   # [20 30 40]   AND
a[(a < 15) | (a > 45)]   # [10 50]      OR
a[~(a > 25)]             # [10 20]      NOT
a[a % 20 == 0]           # [20 40]

m = np.arange(1, 13).reshape(3, 4)
m[m % 2 == 0]            # [ 2  4  6  8 10 12]   result is always 1D