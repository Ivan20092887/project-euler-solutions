sum1 = 0
sum2 = 0
for number in range(1,101):
    sum1 += number**2
    sum2 += number
print(sum2**2 - sum1)
