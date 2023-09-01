str = "jagadish.kumar"
str1 = "python"
str2 = "kumar"
print(str[0])
print(str[0:8])  # substring
print(str + " " + str1)
print(str2 in str)
# to split the string
var = str.split(".")
print(var)
print(var[0])
print()
# TO remove the end white spaces
str4 = "hyderabad            "
print(str4)
print(str4.strip())
print()
# to remove the beginning white spaces
str6="           hyderbad"
print(str6)
print(str6.lstrip())