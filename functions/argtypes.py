#variable length concept
def sum(a, *b):


    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i

    print(c)

sum(1,2,3,5,6)