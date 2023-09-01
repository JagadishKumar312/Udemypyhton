#Finally block will execute at any cost

try:
    with open('logger.txt','r') as reader1:
        reader1.read()

except Exception as e:
    print(e)

finally:
    print("cleanup the resoures")