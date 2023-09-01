
for i in range(4):

     for j in range(4):
         print("#",end="")

     print()

print("end of line")

for i in range(0,5):
    for j in range(i):
        print("#",end="")

    print()
print("break here")

for i in range(0,5):
    for j in range(4-i):
        print("@",end="")

    print()

