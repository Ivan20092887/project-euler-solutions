summ = 23
for number in range(10,1000):
    if number % 3 == 0 or number % 5 == 0:
        summ += number
print(summ)