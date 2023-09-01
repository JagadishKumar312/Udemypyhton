import  sys
def is_even(n):
    return n%2==0

nums = [11,22,46,64,21,73,54,33]

evens = list(filter(is_even,nums))
print(evens)


print()
print("using lambda")
nums = [11,22,46,64,21,73,54,33]

evens = list(filter(lambda n : n%2==0,nums))

print(evens)

