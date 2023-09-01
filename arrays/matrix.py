from numpy import *
arr1 = array([
            [1,2,3,4,],
            [7,8,9,10]

             ])
print(arr1)
m= matrix(arr1)

m= matrix('10,20,30,40 ; 50,11,12,15')
print(m)
print()

m1= matrix('10,20,30 ;40,50,11 ; 12,15,32')
print(m1)
print()
print(diagonal(m1))
print(m1.min())
print(m1.max())