from numpy import *

arr1 = array([
            [1,2,3,4,5,6],
            [7,8,9,10,11,12]

             ])

print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.flatten())
arr2=arr1.reshape(2,2,3)
print(arr2)