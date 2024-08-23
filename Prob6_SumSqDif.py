        
sum2 = 0
for i in range(1, 101):
    sum2 = sum2 + i
sum2 = sum2*sum2

sum1 = 0
for i in range(1, 101):
    n = i * i
    sum1 = sum1 + n

print(sum2 - sum1)