#to open and close the file automatically
#first read the file and store all the elements in the list
#reverse the list
#write the reversed list into the text file


with open('write.txt','r') as reader:
    content=reader.readlines()
    reversed(content)
    with open('write.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)



