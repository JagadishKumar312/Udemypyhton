def person(name, **data):

     print(name)
     print(data)

person('navin',age=28,mob=946459,city='hyd')

print()


def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)


person('navin', age=28, mob=946459, city='hyd')
