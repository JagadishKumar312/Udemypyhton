# try catch mechanism

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("I reached this block because code in try block is a failure")

# to Get the exact Exception

try:
    with open('logger.txt','r') as reader1:
        reader1.read()

except Exception as e:
    print(e)
