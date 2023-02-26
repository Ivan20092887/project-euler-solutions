f1 = 1
f2 = 2
summ = 2
while f1 + f2 < 4000000:
    f = f1 + f2
    if f % 2 == 0:
        summ += f
    f1, f2 = f2, f
print(summ)