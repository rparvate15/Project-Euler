
import math

factorial = math.factorial(100)
sum = 0

for digit in str(factorial): 
      sum += int(digit)

print(sum)