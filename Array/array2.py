# importing array types
import array
from array import *


a = array.array('i', [5, 6, 8, 10, -11])

for i in a:
    print(i, end='   ')
