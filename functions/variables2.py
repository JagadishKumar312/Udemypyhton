a=10
print(id(a))
def something():
    b=30
    x = globals()['a']

    print(b)
    print(x)
    print(id(x))


    globals()['a']=69
    print(a)
    print(id(a))

something()