
lst = [20,25,55,22,224,77,31,44,66,21,88]
def count(lst):

    even=0
    odd=0

    for i in lst:

        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

even,odd = count(lst)

print(even)
print(odd)
print("even: {} and odd : {}".format(even,odd))