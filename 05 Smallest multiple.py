number = 2520
for divisor in range(11,21):
    if number % divisor:
        gcd = divisor // 2
        while number % gcd or divisor % gcd:
            gcd -= 1
        number *= divisor // gcd
print(number)