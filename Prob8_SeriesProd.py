
series = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
listSeries = [int(i) for i in str(series)]
# print(listSeries)

products = []

i = 0
while i < 987:
    x1 = listSeries[i]
    x2 = listSeries[(i + 1)]
    x3 = listSeries[(i + 2)]
    x4 = listSeries[(i + 3)]
    x5 = listSeries[(i + 4)]
    x6 = listSeries[(i + 5)]
    x7 = listSeries[(i + 6)]
    x8 = listSeries[(i + 7)]
    x9 = listSeries[(i + 8)]
    x10 = listSeries[(i + 9)]
    x11 = listSeries[(i + 10)]
    x12 = listSeries[(i + 11)]
    x13 = listSeries[(i + 12)]
    products.append(x1 * x2 * x3 * x4 * x5 * x6 * x7 * x8 * x9 * x10 * x11 * x12 * x13)
    i = i + 1

products.sort()
print(products)