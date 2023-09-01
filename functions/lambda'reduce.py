
nums = [11,22,46,64,21,73,54,33]

evens = list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n: n+2,evens))

print(evens)
print(doubles)

print("evens : {} and doubles : {}",format(evens,doubles))