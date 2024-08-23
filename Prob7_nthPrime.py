
# take number, check prime, if true add to list, if not, increment by 1

PrimeNums = []


def checkPrime(n):
    i = 2
    while i < n + 1:
        if n % i == 0 and n != i:
            return False
        elif n % i != 0:
            i = i + 1
        elif n == i:
            return True

num = 3
while len(PrimeNums) < 10000: 
    if checkPrime(num) == True:
        PrimeNums.append(num)
    num = num + 2
    print(num)

print(PrimeNums)