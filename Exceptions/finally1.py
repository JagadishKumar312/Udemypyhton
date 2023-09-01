try:
    with open('exception.txt','r') as reader:
        content = reader.readlines()
        reversed(content)
        with open('exception.txt','w') as writer:
            for line in reversed(content):
                writer.writelines(line)
except Exception as e:
    print(e)

finally:
    print("task")
