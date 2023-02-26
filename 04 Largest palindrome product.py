max_pal = 0
for f1 in range(999,100,-1):
    for f2 in  range(999,100,-1):
        number = f1 * f2
        if number == int(str(number)[::-1]) and number > max_pal:
            max_pal = number
print(max_pal)