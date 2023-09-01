from numpy import *

arr = array([1,2,3,4,5.0])

print(arr.dtype)
print(arr)

arr1 = linspace(0,15,20)
print(arr1)

arr3 = arange(1,16,2)
print(arr3)

arr4  = logspace(1,10,5)
print(arr4)
print('%.2f' %arr[3])
print()

arr5 = zeros(5)
print(arr5)

arr6 = ones(7,int)
print(arr6)