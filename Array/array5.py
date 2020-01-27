# indexing
# using while loop
from array import *

X = array('i', [10, 20, 30, 40, 50])

n = len(X)

i = 0

while i < n:
    print(X[i], end=' ')
    i += 1
