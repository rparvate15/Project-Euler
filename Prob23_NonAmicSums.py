
# Find sum of all positive integers that can't be written as the sum of 2 abundant numbers.
# All numbers above 28123 can be written as the sum of 2 abundant numbers
# The greatest number that cannot be expressed as the sum of 2 abundant numbers is less than 28123
# 4179871

def get_abun_num(test_num) -> bool:
    """returns if number is abundant number or not"""
    divisor_sum = 0
    for i in range(1, test_num):
        if test_num % i == 0:
            divisor_sum += i
    if divisor_sum > test_num:
        return True
    else:
        return False

abundant_nums = []
all_nums = []
abun_sums = []

# adds all numbers to all_nums array
for i in range(0, 28123):
    all_nums.append(i)

# adds abundant numbers to abundant_nums array
for i in range(1, 28123):
    if get_abun_num(i) == True:
        abundant_nums.append(i)

# adds all abundant sums to sum array
for num1 in abundant_nums:
    for num2 in abundant_nums:
        sum = num1 + num2
        abun_sums.append(sum)

# removing all abundant sums from all nums
for num in abun_sums:
    if num < 28123:
        all_nums[num] = 0

# sums all_nums (sum() wasn't working (int object not callable)??)
end_result = 0
for nums in all_nums:
    end_result += nums

print(end_result)