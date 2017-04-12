string_input = "1, 23, 4, 55,,1,,,33,  ,3,,5,103, 74,3"
highest_value = None

# find highest value and assign to the highest_value variable
# print highest value
split_values = string_input.split(',')

for i in range(len(split_values)):
    split_values[i] = split_values[i].strip()

highest = 0

for v in split_values:
    if len(v) != 0:
        n = int(v)
        if n > highest:
            highest = n

print (highest)


# step1. normalize
# ["1", " ", "0", " ",  1234] a. split by ","
# b.

string_input = "1, 23,4,55,,1,,,33,  ,3,,5,103,  74,3"

split_values = string_input.split(',')

for i in range(len(split_values)):
    split_values[i] = split_values[i].strip()

highest = 0

for v in split_values:
    if len(v) != 0:
        n = int(v)
        if n > highest:
            highest = n


print(highest)
