file = open('readwrite.txt')
#loop to read line by line

line = file.readline()

while line != "":
    print(line)
    line=file.readline()

file.close()

file = open('readwrite.txt')

for line in file.readline():
     print(line)

file.close()