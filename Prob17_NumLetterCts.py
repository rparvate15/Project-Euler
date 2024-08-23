
#  21124

from num2words import num2words

# initialize total array with 1
total_letters = list(num2words(1))

# make for loop with 2-1001 (to include 1000)
# list() each number into different array
# for loop with array.len() to append to the total array
for i in range(2, 1001):
    temp_letters = list(num2words(i))
    for x in range(0, len(temp_letters)):
        total_letters.append(temp_letters[x])
    temp_letters.clear()

# for loop that goes through each thing to remove spaces and hyphens
for y in range(0, len(total_letters) - 1):
    try:
        if total_letters[y] == (" "):
            del total_letters[y]
        elif total_letters[y] == "-":
            del total_letters[y]
    except IndexError:
        break

# len() of total array = answer
print(len(total_letters))