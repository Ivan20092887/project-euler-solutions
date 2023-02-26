number = 600851475143
divisor = 3
while number != 1:
    if number % divisor == 0:
        while number % divisor == 0:
            number //= divisor
    divisor += 2
print(divisor - 2)