
def palindromeTest(num):
    if num != num[::-1]:
        return False
    else:
        return True

palindromeNums = []

for i in range(100, 1000):
    for n in range(100, 1000):
        testnum = i * n
        if palindromeTest(str(testnum)) == False:
            n = n + 1
        elif palindromeTest(str(testnum)) == True:
            palindromeNums.append(testnum)
            n = n + 1
    i = i + 1

palindromeNums.sort()

print(palindromeNums[-1])