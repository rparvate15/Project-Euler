
#numbers copied as string
num_pyramid = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

#splitting the number into a list
num_pyramid = num_pyramid.strip().split('\n')

#converting each and every list of strings to int
for i in range(1,len(num_pyramid)):
	num_pyramid[i] = num_pyramid[i].strip().split(' ')
	num_pyramid[i] = [int(x) for x in num_pyramid[i]]

#adding the first number bcz we could not do the above
#operation as this one one number
num_pyramid[0] = [75]


#for loop for bottom-up approach
for i in range(len(num_pyramid)-2,-1,-1):
	for j in range(len(num_pyramid[i])):
		num_pyramid[i][j] = num_pyramid[i][j] + max(num_pyramid[i+1][j], num_pyramid[i+1][j+1])
	num_pyramid.pop()

#printing the output
print ('The max number is {}'.format(num_pyramid[0][0]))
