# The Fibonacci sequence is defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2) where F(1) = 1 and F(2) = 1
# F(12) is the first term to have 3 digits. What's the index of the first term to have 1000 digits?

# Answer = 4782

# loop to check how many digits in a number
def digitcheck(input):
    count = 0
    while(input > 0):
        count += 1
        input = input // 10
    return count

# creates F(1) and F(2)
fibonacci = [1, 1]

# creates whole list of fibonacci until last term is 1000 digits
while digitcheck(fibonacci[-1]) < 1000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(len(fibonacci))