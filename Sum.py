sum = 0
for i in range(1, 101):
    if i % 3 != 0 and i % 7 != 0 and i % 13 != 0:
        sum = sum+i
print(sum)
