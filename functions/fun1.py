


def greet() :
    print("hello")
    print("good morning")

greet()

def add(x,y):
    z=x+y
    print(z)

add(5,4)

def add1(x,y):
    z=x+y
    return z

result = add1(3,7)
print(result)
print()
def add2_sub(x,y):
    z=x+y
    s=x-y
    return z,s

result1 = add2_sub(90,10)
print(result1)