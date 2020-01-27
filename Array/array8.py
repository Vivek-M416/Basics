# methods of array classes
from array import *
x = array('i', [10, 20, 30, 40, 50])

print('Original array : ', x)

x.append(30)
print('after appending 30', x)

x.insert(1, 90)
print('after inserting', x)

# removeing last element using pop

n = x.pop()
print('after poping :', x)
print('poped element :', n)

# finding position of the element
n = x.index(30)
print('index of the element is :', n)


#converting array to list

lst = x.tolist()
print('list : ', lst)

print('Final Array : ', x)


