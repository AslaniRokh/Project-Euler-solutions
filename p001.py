# solution 1
result = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
print(result)

# solution 2
sum = 0
for item in range(1000):

    if item % 3 == 0 or item % 5 == 0:
        sum += item
print(sum)
