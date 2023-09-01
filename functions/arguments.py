def update(x):
    print(id(x))
    x=10
    print(x)
    print(id(x))

update(8)

a=50
update(a)
print(a)