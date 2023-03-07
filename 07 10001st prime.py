number= 10001
result = 3
count = 1
prime = 2

while count < number:
    for x in range(3, int(result ** 0.5) + 1, 2):
        if result % x == 0:
            break
    else:
        prime = result
        count += 1
    result += 2
print(prime)