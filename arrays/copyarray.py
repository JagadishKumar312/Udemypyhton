from numpy import *

arr1 = array([1,2,3,4,5])



arr2=arr1.copy()
arr1[1]=9
print(arr1)
print(arr2)
print()
print(id(arr1))
print(id(arr2))