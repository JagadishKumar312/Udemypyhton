x=int(input("enter the val"))

r=(x%2)

if r==0:
    print("even")
    if x>10:
        print("greater")
    else:
        print("not greater")
else:
    print("not")
