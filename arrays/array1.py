from  array import *

vals = array('i',[2,5,-6,63,53])
print(vals)
print(vals.buffer_info())
vals.append(90)
print(vals)
vals.remove(vals[1])
print(vals)
vals.reverse()
print(vals)



for i in range(len(vals)):
    print(vals[i])

print("break here-------------------")

newarray = array(vals.typecode,(a for a in vals))

for e in newarray:
    print(e)
