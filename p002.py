# solution 1
# recursive implementation
def fib(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        result = fib(n - 1) + fib(n - 2)
        return result


a = sum(list(filter(lambda x: x % 2 == 0, [fib(i) for i in range(35)])))
print(a)

# solution 2
# generate fib numbers
fibNumber = [0, 1]
while fibNumber[-1] <= 4000000:
    fibNumber.append(fibNumber[-2] + fibNumber[-1])

# find all even numbers
evenFibNumber = []
for item in fibNumber:
    if item % 2 == 0:
        evenFibNumber.append(item)

# sum all of even numbers
totalSum = 0
for even in evenFibNumber:
    totalSum += even
print(totalSum)
