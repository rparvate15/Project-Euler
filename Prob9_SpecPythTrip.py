
d = 0
m = 2

while (d != 1000):
    for n in range(1,m+1):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        d = a + b + c
        if (d == 1000):
            product = a * b * c
            print("Done - " + str(product))
            print(a)
            print(b)
            print(c)
            break
        if (a == 0 or b == 0 or c == 0):
            break
    m += 1