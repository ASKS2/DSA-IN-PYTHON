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