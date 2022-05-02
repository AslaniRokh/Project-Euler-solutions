# solution 1
def prime_number(number):
    factors = []
    i = 2
    while i <= number:
        if number % i == 0:
            factors.append(i)
            number = number // i

        else:
            i += 1
    return factors


print(prime_number(600851475143)[-1])
