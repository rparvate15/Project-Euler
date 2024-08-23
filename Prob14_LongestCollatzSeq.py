
# 837799

terms = []
testnum = 999999
termnum = testnum
term_amount = []

for x in range(1, 999999):
    terms.append(termnum)
    runningnum = termnum
    while terms[-1] != 1:
        if runningnum % 2 == 0:
            runningnum = runningnum/2
        else:
            runningnum = (3 * runningnum) + 1
        terms.append(runningnum)
    # print(str(termnum) + " has " + str(len(terms)) + " terms")
    # term_amount.append(len(terms))
    if len(terms) == 525:
        print(termnum)
    terms.clear()
    termnum = termnum - 1

term_amount.sort()
# print(term_amount)
print("Done")
