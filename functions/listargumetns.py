def update(lst):
    print(id(lst))
    lst[1]=66
    print(id(lst))

    print(" list",lst)

lst = [10,20,30,40]
print(id(lst))
update(lst)

print("list",lst)

