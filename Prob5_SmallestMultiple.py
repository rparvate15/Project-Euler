
rangemax = 20
def div_check(n):
    for i in range(11,rangemax+1):
        if n % i == 0:
            continue
        else:
            print(n)
            return False
            break
    return True

if __name__ == '__main__':
   num = 2520
   while not div_check(num):
       num += 2520

print(num)